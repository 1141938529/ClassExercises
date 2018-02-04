class scoresurface :
    def __init__(self,mfont,score,color,text):
        self.score = score
        self.mfont = mfont
        self.text =text
        self.color= color
        self.surface = self.mfont.render(self.text+str(self.score), True, self.color)

    def refalshsurface(self):
        self.surface = self.mfont.render(self.text + str(self.score), True, self.color)
    pass
