#!/usr/bin/python3

"""
音乐播放器

我们将使用Tkinter和Pygame模块在 Python 中创建一个音乐播放器应用程包括：
    play()：播放/停止 功能
    pause()：暂停/继续播放 功能

库：
    Tkinter：
        是一个非常轻量级的模块，它有助于创建跨平台应用程序，python 自带。
    Pygame:
        是一个与计算机图形和声音库配合使用的 Python 模块，其设计具有播放不同多媒体格式（如音频、视频等）的能力。
        在创建音乐播放器应用程序时，我们将使用 Pygame 的模块来提供不同的 mixer.music 功能，
        我们的音乐播放器应用程序通常与歌曲曲目的操作相关。
        第三方库，需要安装
"""

import os
import tkinter
import pygame


class MusicPlayer(object):
    """
    音乐播放器
    """

    def __init__(self, root, album_path):
        """
        初始化函数
        :param root: 窗口
        :param album_path: 歌曲专辑路径
        """
        # 初始化self.root
        self.root = root

        self.albumPath = album_path

        # 初始化Pygame
        pygame.init()

        # 初始化Pygame Mixer
        pygame.mixer.init()

        # 声明self.track实例属性
        self.track = tkinter.StringVar()

        # 声明self.status实例属性
        self.status = tkinter.StringVar()

        # 控制按钮标签显示
        self.pauseButtonTextVar = tkinter.StringVar()
        self.playButtonTextVar = tkinter.StringVar()

        # Creating the Track Frames for Song label & status label
        track_frame = tkinter.LabelFrame(self.root, text="Track",
                                         font=("times new roman", 15, "bold"),
                                         bg="blue", fg="white", bd=5,
                                         relief=tkinter.GROOVE)
        track_frame.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        track_label = tkinter.Label(track_frame, textvariable=self.track,
                                    width=20,
                                    font=("times new roman", 24, "bold"),
                                    bg="Orange", fg="gold")
        track_label.grid(row=0, column=0, padx=10, pady=10)
        # Inserting Status Label
        status_label = tkinter.Label(track_frame, textvariable=self.status,
                                     width=10,
                                     font=("times new roman", 24, "bold"),
                                     bg="orange", fg="gold")
        self.status.set("Stopped")
        status_label.grid(row=0, column=1, padx=10, pady=10)

        # Creating Button Frame
        control_frame = tkinter.LabelFrame(self.root, text="Control",
                                           font=("times new roman", 15, "bold"),
                                           bg="grey", fg="white", bd=5,
                                           relief=tkinter.GROOVE)
        control_frame.place(x=0, y=100, width=600, height=100)
        # Inserting Play Button
        play_button = tkinter.Button(control_frame, command=self.play,
                                     textvariable=self.playButtonTextVar,
                                     width=10, height=1,
                                     font=("times new roman", 15, "bold"),
                                     fg="blue", bg="pink")
        self.playButtonTextVar.set("播放")
        play_button.grid(row=0, column=0, padx=10, pady=10)
        # Inserting Pause Button
        pause_button = tkinter.Button(control_frame, command=self.pause,
                                      textvariable=self.pauseButtonTextVar,
                                      width=8, height=1,
                                      font=("times new roman", 15, "bold"),
                                      fg="blue", bg="pink")
        self.pauseButtonTextVar.set("暂停")
        pause_button.grid(row=0, column=1, padx=10, pady=10)

        # Creating Playlist Frame
        playlist_frame = tkinter.LabelFrame(self.root, text="Playlist",
                                            font=("times new roman", 15, "bold"),
                                            bg="grey", fg="white", bd=5,
                                            relief=tkinter.GROOVE)
        playlist_frame.place(x=0, y=200, width=600, height=300)
        # Inserting scrollbar
        scrollbar_y = tkinter.Scrollbar(playlist_frame, orient=tkinter.VERTICAL)
        # Inserting Playlist listbox
        self.playlist = tkinter.Listbox(playlist_frame,
                                        yscrollcommand=scrollbar_y.set,
                                        selectbackground="gold",
                                        selectmode=tkinter.SINGLE,
                                        height=300,
                                        font=("times new roman", 12, "bold"),
                                        bg="silver", fg="blue", bd=5,
                                        relief=tkinter.GROOVE)
        # Applying Scrollbar to listbox
        scrollbar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        scrollbar_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=tkinter.BOTH)
        # Changing Directory for fetching Songs
        os.chdir(self.albumPath)
        # Fetching Songs
        songs = os.listdir()
        # Inserting Songs into Playlist
        for song in songs:
            self.playlist.insert(tkinter.END, song)

    def play(self):
        """
        播放歌曲
        :return:
        """
        # 播放/停止，暂停按钮都恢复显示为 "暂停"
        self.pauseButtonTextVar.set("暂停")
        if self.status.get() == "Stopped":
            current = self.playlist.get(tkinter.ACTIVE)
            if current == '':
                return

            # 显示状态
            self.status.set("Playing")
            # 显示选择的歌曲
            self.track.set(current)
            # 载入选择的歌曲
            pygame.mixer.music.load(current)
            # 播放选择的歌曲
            pygame.mixer.music.play()
            # 按钮变为停止
            self.playButtonTextVar.set("停止")
        else:
            # 显示状态
            self.status.set("Stopped")
            # 停止播放
            pygame.mixer.music.stop()
            # 按钮变为播放
            self.playButtonTextVar.set("播放")

    def pause(self):
        """
        暂停播放
        :return:
        """
        if self.status.get() == "Playing":
            # 显示状态
            self.status.set("Paused")
            # 暂停播放
            pygame.mixer.music.pause()
            # 按钮变为恢复播放
            self.pauseButtonTextVar.set("播放")
        elif self.status.get() == "Paused":
            # 显示状态
            self.status.set("Playing")
            # 暂停播放
            pygame.mixer.music.unpause()
            # 按钮变为恢复播放
            self.pauseButtonTextVar.set("暂停")


if __name__ == '__main__':
    root = tkinter.Tk()  # 创建窗口
    root.title("Music Player")  # 设置窗口标题
    root.geometry("600x500+200+200")  # 设置窗口大小
    MusicPlayer(root, "./music")
    root.mainloop()
