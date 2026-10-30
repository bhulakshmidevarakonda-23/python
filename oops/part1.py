class myname():
    
    def name1(self,name="bhulu"):
        self.name=name
        print(f"my name is {name}")#my name is bhulu
    def name2(self,initial="devarakonda"):
        self.initial=initial
        print(f"my initial was {initial}")#my initial was devarakonda
obj=myname()
obj.name1()
obj.name2()
