import tkinter as tk
from tkinter.filedialog import askopenfilename
from srt_burner import EncodeJob
from os.path import splitext

class MainAppWindow(tk.Frame):
    def __init__(self, master=None):
        self.sub_path = tk.StringVar()
        self.vid_path = tk.StringVar()
        
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    
    def createWidgets(self):

        # labels for each file type entry field
        self.lbl_mp4 = tk.Label(self, text="Choose Video File: ")
        self.lbl_srt = tk.Label(self, text="Choose Subtitle File: ")
        self.lbl_mp4.grid(sticky="E", column=0, row=0)        
        self.lbl_srt.grid(sticky="E", column=0, row=1)

        # entry fields for each file
        self.entry_vidpath = tk.Entry(self, textvariable=self.vid_path, width=30)
        self.entry_srtpath = tk.Entry(self, textvariable=self.sub_path, width=30)
        self.entry_vidpath.grid(column=1, row=0)
        self.entry_srtpath.grid(column=1, row=1)
        
        # buttons (Browse) for picking each file
        self.btn_pick_vid = tk.Button(self, text="Browse", command= lambda: self.choose_file("vid"))
        self.btn_pick_srt = tk.Button(self, text="Browse", command= lambda: self.choose_file("sub"))
        self.btn_pick_vid.grid(column=2, row="0")
        self.btn_pick_srt.grid(column=2, row="1")
        
        self.btn_start = tk.Button(self, text="Start", command=self.start_encode)
        self.btn_start.grid(sticky="E", column=1, row=2)
        # Quit
        self.QUIT = tk.Button(self, text="Quit", command=root.destroy)
        self.QUIT.grid(sticky="E", column=2, row=2)

    def choose_file(self, filetype):
        if filetype == "sub":
            srt_path = askopenfilename(title="Select SRT", \
                filetypes=[("SRT Files","*.srt")])
            self.sub_path.set(srt_path)

        elif filetype == "vid":
            vid_path = askopenfilename(title="Select Video", \
                filetypes=[("MP4 Files","*.mp4")])
            self.vid_path.set(vid_path)

    def start_encode(self):
        job = EncodeJob(vid_path=self.vid_path.get(), sub_path=self.sub_path.get(), 
            out_path=f"{self.vid_path.get().splitext()[0]}_subbed.mp4")
        job.start()

root = tk.Tk()
root.title("srt-burner")
app = MainAppWindow(master=root)

app.mainloop()