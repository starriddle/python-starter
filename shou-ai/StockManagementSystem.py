#!/usr/bin/python3

"""
库存管理系统

使用面向对象的方法设计一个库存管理系统，具备以下功能：

商品入库
- 输入商品名称，价格，数量，序列号，进行入库操作。
- 处理逻辑：
  1 若库存为空，则将当前商品信息加入库存列表
  2 若库存不为空
    2.1 通过遍历库存列表，比较商品编号，确认库中是否有当前商品。
    2.2 若有当前商品，则增加当前商品数量，然后退出遍历。
    2.3 若没有当前商品，则将当前商品信息加入库存列表

商品出库
- 输入商品名称或序列号和数量出库，处理商品重名情况，进行出库操作。
- 处理逻辑：
  1 查找对应的商品(根据输入的信息去查找)
    - 遍历库存列表，用 index / name 去查找商品，将对应商品的索引放入索引列表。
  3 处理冲突问题
    - 索引列表只有 1 个元素，没问题，直接取出
    - 索引列表为空，找不到商品，不执行出库操作
    - 索引列表含有多个元素，发生冲突，进一步选择
      3.1 依次输出索引(序号)，以及对应商品信息
      3.2 获取输入的序号，作为最终结果取出
  4 取出选择的商品
    - 根据最终索引获取对应商品库存信息
      - 若库存数量不小于要取出的数量，则更新库存数量，输出出库成功信息。
      - 若库存数量小于要取出的数量，则输出出库失败信息

商品查询
- 输入商品名称或序列号查询。
- 处理逻辑：
  1 查找对应的商品(根据输入的信息去查找)
    - 遍历库存列表，用 index / name 去查找商品，放入结果列表。
  3 打印查找到的商品列表：若print_flag为true，则打印结果列表
  4 返回结果列表

库存统计
- 统计商品类型数量，商品总数量，商品总价值。
- 通过默认最小库存参数显示库存不足商品。
- 通过设置最小库存参数显示库存不足商品。

导出 TXT
- 将商品列表导出至文件。
- 处理逻辑：
  1 若商品列表为空，则返回。
  2 若商品列表不为空，遍历商品列表，每行以(good.name, good.price, good.number, good.index)的格式将商品信息输出到 GOODS.txt 文件。

导出 EXCEL
- 将商品列表导出至EXCEL。
- 处理逻辑：
  1 建立excel工作簿。
  2 建立工作表。
  3 在第一行写入表头：名称，价格，数量，编号。
  4 遍历商品列表，将商品信息输入文件。
  5 保存文件为 GOODS.xls

导入 TXT
- 从文件导入商品列表
- 处理逻辑：
  1 读取 GOODS.txt 文件
  2 每行以(good.name, good.price, good.number, good.index)的格式转换为商品信息
  3 将所有商品保存到库存列表

导入 EXCEL
- 从EXCEL导入商品列表。
- 处理逻辑：
  1 读取 excel 工作簿
  2 读取工作表
  3 除了标题行，读取每行数据转换为商品信息
  4 将所有商品信息保存到库存列表

第三方库：
- pandas: 可以读取各种各样格式的数据文件，支持 txt、csv、excel、json、剪切板、数据库、html、hdf、parquet、pickled文件、sas、stata等等
- xlrd: 从 excel 中读取数据，支持 xls 和 xlsx
- xlwt: 对 excel 进行修改操作，支持 xls，不支持 xlsx
- xlutils: 在 xlwt 和 xlrd 中，对一个已存在的文件进行修改
- xlsxwriter: 生成 excel 表格，插入数据、插入图表等表格操作，不支持读取
- openpyxl: 对 xlsx 文件进行读取和编辑
- xlwings: 对 xls 、xlsx、xlsm 文件进行读写、格式修改等操作
"""
import copy

import xlrd
import xlwt


class Product(object):
    """
    商品类
    """

    def __init__(self, name="", price=0.0, number=0, index=""):
        """
        初始化函数
        :param name: 商品名
        :param price: 商品价格
        :param number: 商品数量
        :param index: 商品编号
        """
        self.name = name
        self.price = price
        self.number = number
        self.index = index

    def set_name(self, name):
        """
        设置商品名称
        :param name: 商品名称
        :return:
        """
        self.name = name

    def set_price(self, price):
        """
        设置商品价格
        :param price: 商品价格
        :return:
        """
        self.price = price

    def set_number(self, number):
        """
        设置商品数量
        :param number: 商品数量
        :return:
        """
        self.number = number

    def set_index(self, index):
        """
        设置商品编号
        :param index: 商品编号
        :return:
        """
        self.index = index

    def format_print(self):
        """
        格式化打印产品信息
        :return:
        """
        n = 0
        for c in self.name:
            n += 1 if ord(c) < 128 else 2
        name_str = self.name + ' ' * (10 - n)
        print("商品编号: {} | 商品名称: {} | 商品数量: {:5d} | 商品价格: {:8.2f}"
              .format(self.index, name_str, self.number, self.price))


class Stock(object):
    """
    库存类
    """

    def __init__(self):
        """
        初始化函数
        """
        self.goods = []

    def set_goods(self, goods):
        """
        设置库存中的商品列表
        :param goods: 商品列表
        :return:
        """
        self.goods = goods

    def get_goods(self):
        """
        获取库存中的商品列表
        :return: 商品列表(深度复制)信息
        """
        return copy.deepcopy(self.goods)

    def list(self):
        """
        显示所有商品列表
        :return:
        """
        print("=============================================================================")
        print("                                所有商品列表                                 ")
        print("-----------------------------------------------------------------------------")
        for good in self.goods:
            good.format_print()
        print("=============================================================================")

    def statistics(self, min_number=15):
        """
        统计商品信息：总数量，总价值
        通过自定义最小库存数量，显示库存告急的商品列表
        :param min_number: 最小库存数量
        :return:
        """
        total_number = 0
        total_amount = 0.0
        lack_goods = []
        for good in self.goods:
            total_number += good.number
            total_amount += good.number * good.price
            if good.number < min_number:
                lack_goods.append(good)
        print("=============================================================================")
        print("                                商品统计信息                                 ")
        print("-----------------------------------------------------------------------------")
        print("总计：\n"
              "        商品种类: {}\n"
              "        商品总数: {}\n"
              "        商品总额: {}\n"
              "库存不足商品种类: {}"
              .format(len(self.goods), total_number, total_amount, len(lack_goods)))
        print("-----------------------------------------------------------------------------")
        print("                              库存不足商品列表                               ")
        print("-----------------------------------------------------------------------------")
        for good in lack_goods:
            good.format_print()
        print("=============================================================================")

    def stock_in(self, product):
        """
        商品入库
        :param product: 入库商品
        :return:
        """
        exists = False
        if len(self.goods) > 0:
            for good in self.goods:
                if good.index == product.index:
                    good.number += product.number
                    exists = True
                    break
        if not exists:
            self.goods.append(product)

    def stack_out(self, product):
        """
        商品出库
        :param product: 出库商品
        :return:
        """
        idx_list = []
        # 查找商品
        if product.index != "" and product.name == "":
            for i in range(len(self.goods)):
                if product.index == self.goods[i].index:
                    idx_list.append(i)
        elif product.index == "" and product.name != "":
            for i in range(len(self.goods)):
                if product.name == self.goods[i].name:
                    idx_list.append(i)
        # 处理问题
        selected_idx = 0
        if len(idx_list) == 0:
            print("ROBOT：未找到商品！")
            return
        elif len(idx_list) == 1:
            selected_idx = idx_list[0]
        else:
            print("ROBOT：找到多个商品")
            for idx in idx_list:
                print("[ {} ] ".format(idx), end="")
                self.goods[idx].format_print()
            selected_idx = int(input("ROBOT：请选择序号："))
        # 商品出库
        if product.number <= self.goods[selected_idx].number:
            self.goods[selected_idx].number -= product.number
            print("ROBOT：成功取出商品，剩余商品信息：")
            self.goods[selected_idx].format_print()
            if self.goods[selected_idx].number == 0:
                self.goods.pop(selected_idx)
        else:
            good = self.goods[selected_idx]
            print("ROBOT：无法取出商品，商品库存不足：")
            print("商品编号：{} | 商品名称：{} | 剩余数量：{} | 预取数量：{}"
                  .format(good.index, good.name, good.number, product.number))

    def search(self, product, print_flag=True):
        """
        查找商品，返回找到的商品列表
        :param product: 待查找的商品信息
        :param print_flag: 是否输出查找结果信息
        :return: 找到的商品列表
        """
        results = []
        # 查找商品
        if product.index != "" and product.name == "":
            for good in self.goods:
                if product.index == good.index:
                    results.append(good)
        elif product.index == "" and product.name != "":
            for good in self.goods:
                if product.name == good.name:
                    results.append(good)
        # 输出查找结果
        if print_flag:
            print("=============================================================================")
            print("                              商品查询结果列表                               ")
            print("-----------------------------------------------------------------------------")
            if len(results) == 0:
                print("ROBOT：商品未找到，该商品不在库存中！")
            else:
                for result in results:
                    result.format_print()
            print("=============================================================================")
        # 返回查找结果列表
        return results


class StockIO(object):
    """
    库存 IO 类，用于导入/导出库存信息
    """

    @staticmethod
    def export_to_txt(stock, file_path):
        """
        导出库存列表到 TXT 文件
        :param stock: 库存
        :param file_path: TXT 文件路径
        :return:
        """
        goods = stock.get_goods()
        if len(goods) == 0:
            print("库存为空！")
            return
        f = open(file_path, "w", encoding="UTF-8")
        for good in goods:
            line = "{}, {}, {}, {}\n".format(good.name, good.price, good.number, good.index)
            f.writelines(line)
        f.close()
        print("导出到 TXT 文件成功！")

    @staticmethod
    def import_from_txt(stock, file_path):
        """
        从 TXT 文件导入库存列表
        :param stock: 库存
        :param file_path: TXT 文件路径
        :return:
        """
        f = open(file_path, "r", encoding="UTF-8")
        lines = f.readlines()
        f.close()
        goods = []
        print("=============================================================================")
        print("                           从 TXT 文件导入库存信息                           ")
        print("预计导入商品 %d 种" % (len(lines)))
        print("-----------------------------------------------------------------------------")
        for line in lines:
            strs = line.split(",")
            good = Product(strs[0].strip(), float(strs[1].strip()),
                           int(strs[2].strip()), strs[3].strip())
            good.format_print()
            goods.append(good)
        print("=============================================================================")
        stock.set_goods(goods)
        print("从 TXT 文件导入成功！")

    @staticmethod
    def export_to_excel(stock, excel_path):
        """
        导出库存列表到 EXCEL 文件
        :param stock: 库存
        :param excel_path: EXCEL 文件路径
        :return:
        """
        goods = stock.get_goods()
        if len(goods) == 0:
            print("库存为空！")
            return
        book = xlwt.Workbook(encoding="UTF-8")
        sheet = book.add_sheet("库存列表")
        row = 0
        sheet.write(row, 0, "名称")
        sheet.write(row, 1, "价格")
        sheet.write(row, 2, "数量")
        sheet.write(row, 3, "编号")
        for good in goods:
            row += 1
            sheet.write(row, 0, good.name)
            sheet.write(row, 1, good.price)
            sheet.write(row, 2, good.number)
            sheet.write(row, 3, good.index)
        book.save(excel_path)
        print("导出到 EXCEL 文件成功！")

    @staticmethod
    def import_from_excel(stock, excel_path):
        """
        从 EXCEL 文件导入库存列表
        :param stock: 库存
        :param excel_path: EXCEL 文件路径
        :return:
        """
        book = xlrd.open_workbook(excel_path)
        sheet = book.sheet_by_name("库存列表")
        print("=============================================================================")
        print("                          从 EXCEL 文件导入库存信息                          ")
        print("预计导入商品 %d 种" % (sheet.nrows - 1))
        print("-----------------------------------------------------------------------------")
        goods = []
        for row in range(1, sheet.nrows):
            name = str(sheet.cell(row, 0).value)
            price = float(sheet.cell(row, 1).value)
            number = int(sheet.cell(row, 2).value)
            index = str(sheet.cell(row, 3).value)
            good = Product(name, price, number, index)
            good.format_print()
            goods.append(good)
        print("=============================================================================")
        stock.set_goods(goods)
        print("从 EXCEL 文件导入成功！")


if __name__ == "__main__":
    stock = Stock()
    while True:
        print("\n操作指南：\n"
              "    E: 退出程序，L：商品列表\n"
              "    I：商品入库，O：商品出库，S：商品查询\n"
              "    S1：库存统计(默认参数)，S2：库存统计(设置参数)\n"
              "    OF：导出商品列表至文件，IF：从文件导入商品列表\n"
              "    OE：导出商品列表至EXCEL，IE：从EXCEL导入商品列表")
        key = input("请输入操作指令：").lower()
        if key == 'e':  # 退出程序
            break
        elif key == 'l':  # 商品列表
            stock.list()
        elif key == 'i':
            name, price, number, index = (input("请输入商品名称 价格 数量 编号：").split())
            stock.stock_in(Product(name, float(price), int(number), index))
            stock.list()
        elif key == 'o':
            selected = int(input("请选择 0-商品名称 或 1-商品编号："))
            s = input("请输入商品名称：") if selected == 0 else input("请输入商品编号：")
            number = int(input("请输入商品数量："))
            product = Product(name=s, number=number) if selected == 0 else Product(number=number, index=s)
            stock.stack_out(product)
        elif key == 's':
            selected = int(input("请选择 0-商品名称 或 1-商品编号："))
            s = input("请输入商品名称：") if selected == 0 else input("请输入商品编号：")
            product = Product(name=s) if selected == 0 else Product(index=s)
            stock.search(product)
        elif key == 's1':  # 库存统计
            stock.statistics()
        elif key == 's2':  # 库存统计
            min_number = int(input("请输入商品库存下限："))
            stock.statistics(min_number)
        elif key == 'of':  # 导出到 TXT
            StockIO.export_to_txt(stock, 'GOODS.txt')
        elif key == 'if':  # 从 TXT 导入
            StockIO.import_from_txt(stock, 'GOODS.txt')
        elif key == 'oe':  # 导出到 EXCEL
            StockIO.export_to_excel(stock, 'GOODS.xls')
        elif key == 'ie':  # 从 EXCEL 导入
            StockIO.import_from_excel(stock, 'GOODS.xls')
