class Record:

    def __init__(self):
        valid_types = ["mx","cname","a","soa"]
        self.rtype = None
        self.name = None
        self.rclass = None
        self.rdata = None
        self.ttl = 0

    def set_rtype(self,record_type: str):
        self.rtype = record_type
    def set_name(self,name:str):
        self.name = name
    def set_rclass(self,record_class: str):
        self.rclass = record_class
    def set_rdata(self,record_data:dict):
        self.rdata = record_data
    def set_ttl(self,ttl:int):
        self.ttl = ttl

    def __str__(self):
        return "{0}:{1} -> {2}".format(self.rtype,self.name,self.rdata)

    def validate(self):
        # TODO make this work
        return True



