from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class SimulationResults(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'Results'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False)
    strength1 = Column(Float, index=True, unique=False)
    notorietyratio1 = Column(Float, index=True, unique=False)
    totalextort1 = Column(Float, index=True, unique=False)
    countextort1 = Column(Float, index=True, unique=False)
    countbenefit1 = Column(Float, index=True, unique=False)
    countpunish1 = Column(Float, index=True, unique=False)
    countsupport1 = Column(Float, index=True, unique=False)
    totalsupport1 = Column(Float, index=True, unique=False)
    countdefend1 = Column(Float, index=True, unique=False)
    strength2 = Column(Float, index=True, unique=False)
    notorietyratio2 = Column(Float, index=True, unique=False)
    totalextort2 = Column(Float, index=True, unique=False)
    countextort2 = Column(Float, index=True, unique=False)
    countbenefit2 = Column(Float, index=True, unique=False)
    countpunish2 = Column(Float, index=True, unique=False)
    countsupport2 = Column(Float, index=True, unique=False)
    totalsupport2 = Column(Float, index=True, unique=False)
    countdefend2 = Column(Float, index=True, unique=False)
    strength3 = Column(Float, index=True, unique=False)
    notorietyratio3 = Column(Float, index=True, unique=False)
    totalextort3 = Column(Float, index=True, unique=False)
    countextort3 = Column(Float, index=True, unique=False)
    countbenefit3 = Column(Float, index=True, unique=False)
    countpunish3 = Column(Float, index=True, unique=False)
    countsupport3 = Column(Float, index=True, unique=False)
    totalsupport3 = Column(Float, index=True, unique=False)
    countdefend3 = Column(Float, index=True, unique=False)
    strength4 = Column(Float, index=True, unique=False)
    notorietyratio4 = Column(Float, index=True, unique=False)
    totalextort4 = Column(Float, index=True, unique=False)
    countextort4 = Column(Float, index=True, unique=False)
    countbenefit4 = Column(Float, index=True, unique=False)
    countpunish4 = Column(Float, index=True, unique=False)
    countsupport4 = Column(Float, index=True, unique=False)
    totalsupport4 = Column(Float, index=True, unique=False)
    countdefend4 = Column(Float, index=True, unique=False)
    strength5 = Column(Float, index=True, unique=False)
    notorietyratio5 = Column(Float, index=True, unique=False)
    totalextort5 = Column(Float, index=True, unique=False)
    countextort5 = Column(Float, index=True, unique=False)
    countbenefit5 = Column(Float, index=True, unique=False)
    countpunish5 = Column(Float, index=True, unique=False)
    countsupport5 = Column(Float, index=True, unique=False)
    totalsupport5 = Column(Float, index=True, unique=False)
    countdefend5 = Column(Float, index=True, unique=False)
    strength6 = Column(Float, index=True, unique=False)
    notorietyratio6 = Column(Float, index=True, unique=False)
    totalextort6 = Column(Float, index=True, unique=False)
    countextort6 = Column(Float, index=True, unique=False)
    countbenefit6 = Column(Float, index=True, unique=False)
    countpunish6 = Column(Float, index=True, unique=False)
    countsupport6 = Column(Float, index=True, unique=False)
    totalsupport6 = Column(Float, index=True, unique=False)
    countdefend6 = Column(Float, index=True, unique=False)
    strength7 = Column(Float, index=True, unique=False)
    notorietyratio7 = Column(Float, index=True, unique=False)
    totalextort7 = Column(Float, index=True, unique=False)
    countextort7 = Column(Float, index=True, unique=False)
    countbenefit7 = Column(Float, index=True, unique=False)
    countpunish7 = Column(Float, index=True, unique=False)
    countsupport7 = Column(Float, index=True, unique=False)
    totalsupport7 = Column(Float, index=True, unique=False)
    countdefend7 = Column(Float, index=True, unique=False)
    strength8 = Column(Float, index=True, unique=False)
    notorietyratio8 = Column(Float, index=True, unique=False)
    totalextort8 = Column(Float, index=True, unique=False)
    countextort8 = Column(Float, index=True, unique=False)
    countbenefit8 = Column(Float, index=True, unique=False)
    countpunish8 = Column(Float, index=True, unique=False)
    countsupport8 = Column(Float, index=True, unique=False)
    totalsupport8 = Column(Float, index=True, unique=False)
    countdefend8 = Column(Float, index=True, unique=False)
    strength9 = Column(Float, index=True, unique=False)
    notorietyratio9 = Column(Float, index=True, unique=False)
    totalextort9 = Column(Float, index=True, unique=False)
    countextort9 = Column(Float, index=True, unique=False)
    countbenefit9 = Column(Float, index=True, unique=False)
    countpunish9 = Column(Float, index=True, unique=False)
    countsupport9 = Column(Float, index=True, unique=False)
    totalsupport9 = Column(Float, index=True, unique=False)
    countdefend9 = Column(Float, index=True, unique=False)
    strength10 = Column(Float, index=True, unique=False)
    notorietyratio10 = Column(Float, index=True, unique=False)
    totalextort10 = Column(Float, index=True, unique=False)
    countextort10 = Column(Float, index=True, unique=False)
    countbenefit10 = Column(Float, index=True, unique=False)
    countpunish10 = Column(Float, index=True, unique=False)
    countsupport10 = Column(Float, index=True, unique=False)
    totalsupport10 = Column(Float, index=True, unique=False)
    countdefend10 = Column(Float, index=True, unique=False)
    strength11 = Column(Float, index=True, unique=False)
    notorietyratio11 = Column(Float, index=True, unique=False)
    totalextort11 = Column(Float, index=True, unique=False)
    countextort11 = Column(Float, index=True, unique=False)
    countbenefit11 = Column(Float, index=True, unique=False)
    countpunish11 = Column(Float, index=True, unique=False)
    countsupport11 = Column(Float, index=True, unique=False)
    totalsupport11 = Column(Float, index=True, unique=False)
    countdefend11 = Column(Float, index=True, unique=False)
    strength12 = Column(Float, index=True, unique=False)
    notorietyratio12 = Column(Float, index=True, unique=False)
    totalextort12 = Column(Float, index=True, unique=False)
    countextort12 = Column(Float, index=True, unique=False)
    countbenefit12 = Column(Float, index=True, unique=False)
    countpunish12 = Column(Float, index=True, unique=False)
    countsupport12 = Column(Float, index=True, unique=False)
    totalsupport12 = Column(Float, index=True, unique=False)
    countdefend12 = Column(Float, index=True, unique=False)
    strength13 = Column(Float, index=True, unique=False)
    notorietyratio13 = Column(Float, index=True, unique=False)
    totalextort13 = Column(Float, index=True, unique=False)
    countextort13 = Column(Float, index=True, unique=False)
    countbenefit13 = Column(Float, index=True, unique=False)
    countpunish13 = Column(Float, index=True, unique=False)
    countsupport13 = Column(Float, index=True, unique=False)
    totalsupport13 = Column(Float, index=True, unique=False)
    countdefend13 = Column(Float, index=True, unique=False)
    strength14 = Column(Float, index=True, unique=False)
    notorietyratio14 = Column(Float, index=True, unique=False)
    totalextort14 = Column(Float, index=True, unique=False)
    countextort14 = Column(Float, index=True, unique=False)
    countbenefit14 = Column(Float, index=True, unique=False)
    countpunish14 = Column(Float, index=True, unique=False)
    countsupport14 = Column(Float, index=True, unique=False)
    totalsupport14 = Column(Float, index=True, unique=False)
    countdefend14 = Column(Float, index=True, unique=False)
    strength15 = Column(Float, index=True, unique=False)
    notorietyratio15 = Column(Float, index=True, unique=False)
    totalextort15 = Column(Float, index=True, unique=False)
    countextort15 = Column(Float, index=True, unique=False)
    countbenefit15 = Column(Float, index=True, unique=False)
    countpunish15 = Column(Float, index=True, unique=False)
    countsupport15 = Column(Float, index=True, unique=False)
    totalsupport15 = Column(Float, index=True, unique=False)
    countdefend15 = Column(Float, index=True, unique=False)
    community1m1 = Column(Float, index=True, unique=False)
    community2m1 = Column(Float, index=True, unique=False)
    community3m1 = Column(Float, index=True, unique=False)
    community4m1 = Column(Float, index=True, unique=False)
    community5m1 = Column(Float, index=True, unique=False)
    community6m1 = Column(Float, index=True, unique=False)
    community7m1 = Column(Float, index=True, unique=False)
    community8m1 = Column(Float, index=True, unique=False)
    community9m1 = Column(Float, index=True, unique=False)
    community10m1 = Column(Float, index=True, unique=False)
    community11m1 = Column(Float, index=True, unique=False)
    community12m1 = Column(Float, index=True, unique=False)
    community13m1 = Column(Float, index=True, unique=False)
    community14m1 = Column(Float, index=True, unique=False)
    community15m1 = Column(Float, index=True, unique=False)
    community1m2 = Column(Float, index=True, unique=False)
    community2m2 = Column(Float, index=True, unique=False)
    community3m2 = Column(Float, index=True, unique=False)
    community4m2 = Column(Float, index=True, unique=False)
    community5m2 = Column(Float, index=True, unique=False)
    community6m2 = Column(Float, index=True, unique=False)
    community7m2 = Column(Float, index=True, unique=False)
    community8m2 = Column(Float, index=True, unique=False)
    community9m2 = Column(Float, index=True, unique=False)
    community10m2 = Column(Float, index=True, unique=False)
    community11m2 = Column(Float, index=True, unique=False)
    community12m2 = Column(Float, index=True, unique=False)
    community13m2 = Column(Float, index=True, unique=False)
    community14m2 = Column(Float, index=True, unique=False)
    community15m2 = Column(Float, index=True, unique=False)
    community1m3 = Column(Float, index=True, unique=False)
    community2m3 = Column(Float, index=True, unique=False)
    community3m3 = Column(Float, index=True, unique=False)
    community4m3 = Column(Float, index=True, unique=False)
    community5m3 = Column(Float, index=True, unique=False)
    community6m3 = Column(Float, index=True, unique=False)
    community7m3 = Column(Float, index=True, unique=False)
    community8m3 = Column(Float, index=True, unique=False)
    community9m3 = Column(Float, index=True, unique=False)
    community10m3 = Column(Float, index=True, unique=False)
    community11m3 = Column(Float, index=True, unique=False)
    community12m3 = Column(Float, index=True, unique=False)
    community13m3 = Column(Float, index=True, unique=False)
    community14m3 = Column(Float, index=True, unique=False)
    community15m3 = Column(Float, index=True, unique=False)
    community1m4 = Column(Float, index=True, unique=False)
    community2m4 = Column(Float, index=True, unique=False)
    community3m4 = Column(Float, index=True, unique=False)
    community4m4 = Column(Float, index=True, unique=False)
    community5m4 = Column(Float, index=True, unique=False)
    community6m4 = Column(Float, index=True, unique=False)
    community7m4 = Column(Float, index=True, unique=False)
    community8m4 = Column(Float, index=True, unique=False)
    community9m4 = Column(Float, index=True, unique=False)
    community10m4 = Column(Float, index=True, unique=False)
    community11m4 = Column(Float, index=True, unique=False)
    community12m4 = Column(Float, index=True, unique=False)
    community13m4 = Column(Float, index=True, unique=False)
    community14m4 = Column(Float, index=True, unique=False)
    community15m4 = Column(Float, index=True, unique=False)
    community1m5 = Column(Float, index=True, unique=False)
    community2m5 = Column(Float, index=True, unique=False)
    community3m5 = Column(Float, index=True, unique=False)
    community4m5 = Column(Float, index=True, unique=False)
    community5m5 = Column(Float, index=True, unique=False)
    community6m5 = Column(Float, index=True, unique=False)
    community7m5 = Column(Float, index=True, unique=False)
    community8m5 = Column(Float, index=True, unique=False)
    community9m5 = Column(Float, index=True, unique=False)
    community10m5 = Column(Float, index=True, unique=False)
    community11m5 = Column(Float, index=True, unique=False)
    community12m5 = Column(Float, index=True, unique=False)
    community13m5 = Column(Float, index=True, unique=False)
    community14m5 = Column(Float, index=True, unique=False)
    community15m5 = Column(Float, index=True, unique=False)
    community1m6 = Column(Float, index=True, unique=False)
    community2m6 = Column(Float, index=True, unique=False)
    community3m6 = Column(Float, index=True, unique=False)
    community4m6 = Column(Float, index=True, unique=False)
    community5m6 = Column(Float, index=True, unique=False)
    community6m6 = Column(Float, index=True, unique=False)
    community7m6 = Column(Float, index=True, unique=False)
    community8m6 = Column(Float, index=True, unique=False)
    community9m6 = Column(Float, index=True, unique=False)
    community10m6 = Column(Float, index=True, unique=False)
    community11m6 = Column(Float, index=True, unique=False)
    community12m6 = Column(Float, index=True, unique=False)
    community13m6 = Column(Float, index=True, unique=False)
    community14m6 = Column(Float, index=True, unique=False)
    community15m6 = Column(Float, index=True, unique=False)
    community1m7 = Column(Float, index=True, unique=False)
    community2m7 = Column(Float, index=True, unique=False)
    community3m7 = Column(Float, index=True, unique=False)
    community4m7 = Column(Float, index=True, unique=False)
    community5m7 = Column(Float, index=True, unique=False)
    community6m7 = Column(Float, index=True, unique=False)
    community7m7 = Column(Float, index=True, unique=False)
    community8m7 = Column(Float, index=True, unique=False)
    community9m7 = Column(Float, index=True, unique=False)
    community10m7 = Column(Float, index=True, unique=False)
    community11m7 = Column(Float, index=True, unique=False)
    community12m7 = Column(Float, index=True, unique=False)
    community13m7 = Column(Float, index=True, unique=False)
    community14m7 = Column(Float, index=True, unique=False)
    community15m7 = Column(Float, index=True, unique=False)
    community1m8 = Column(Float, index=True, unique=False)
    community2m8 = Column(Float, index=True, unique=False)
    community3m8 = Column(Float, index=True, unique=False)
    community4m8 = Column(Float, index=True, unique=False)
    community5m8 = Column(Float, index=True, unique=False)
    community6m8 = Column(Float, index=True, unique=False)
    community7m8 = Column(Float, index=True, unique=False)
    community8m8 = Column(Float, index=True, unique=False)
    community9m8 = Column(Float, index=True, unique=False)

def testexcel():
    t = time()

    #Create the database
    engine = create_engine('sqlite:///csv_test.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "test.csv"
        data = Load_Data(file_name)

        for i in data:
            record = SimulationResults(**{
                'strength1' : i[0],
                'notorietyratio1' : i[1],
                'totalextort1' : i[2],
                'countextort1' : i[3],
                'countbenefit1' : i[4],
                'countpunish1' : i[5],
                'countsupport1' : i[6],
                'totalsupport1' : i[7],
                'countdefend1' : i[8],
                'strength2' : i[9],
                'notorietyratio2' : i[10],
                'totalextort2' : i[11],
                'countextort2' : i[12],
                'countbenefit2' : i[13],
                'countpunish2' : i[14],
                'countsupport2' : i[15],
                'totalsupport2' : i[16],
                'countdefend2' : i[17],
                'strength3' : i[18],
                'notorietyratio3' : i[19],
                'totalextort3' : i[20],
                'countextort3' : i[21],
                'countbenefit3' : i[22],
                'countpunish3' : i[23],
                'countsupport3' : i[24],
                'totalsupport3' : i[25],
                'countdefend3' : i[26],
                'strength4' : i[27],
                'notorietyratio4' : i[28],
                'totalextort4' : i[29],
                'countextort4' : i[30],
                'countbenefit4' : i[31],
                'countpunish4' : i[32],
                'countsupport4' : i[33],
                'totalsupport4' : i[34],
                'countdefend4' : i[35],
                'strength5' : i[36],
                'notorietyratio5' : i[37],
                'totalextort5' : i[38],
                'countextort5' : i[39],
                'countbenefit5' : i[40],
                'countpunish5' : i[41],
                'countsupport5' : i[42],
                'totalsupport5' : i[43],
                'countdefend5' : i[44],
                'strength6' : i[45],
                'notorietyratio6' : i[46],
                'totalextort6' : i[47],
                'countextort6' : i[48],
                'countbenefit6' : i[49],
                'countpunish6' : i[50],
                'countsupport6' : i[51],
                'totalsupport6' : i[52],
                'countdefend6' : i[53],
                'strength7' : i[54],
                'notorietyratio7' : i[55],
                'totalextort7' : i[56],
                'countextort7' : i[57],
                'countbenefit7' : i[58],
                'countpunish7' : i[59],
                'countsupport7' : i[60],
                'totalsupport7' : i[61],
                'countdefend7' : i[62],
                'strength8' : i[63],
                'notorietyratio8' : i[64],
                'totalextort8' : i[65],
                'countextort8' : i[66],
                'countbenefit8' : i[67],
                'countpunish8' : i[68],
                'countsupport8' : i[69],
                'totalsupport8' : i[70],
                'countdefend8' : i[71],
                'strength9' : i[72],
                'notorietyratio9' : i[73],
                'totalextort9' : i[74],
                'countextort9' : i[75],
                'countbenefit9' : i[76],
                'countpunish9' : i[77],
                'countsupport9' : i[78],
                'totalsupport9' : i[79],
                'countdefend9' : i[80],
                'strength10' : i[81],
                'notorietyratio10' : i[82],
                'totalextort10' : i[83],
                'countextort10' : i[84],
                'countbenefit10' : i[85],
                'countpunish10' : i[86],
                'countsupport10' : i[87],
                'totalsupport10' : i[88],
                'countdefend10' : i[89],
                'strength11' : i[90],
                'notorietyratio11' : i[91],
                'totalextort11' : i[92],
                'countextort11' : i[93],
                'countbenefit11' : i[94],
                'countpunish11' : i[95],
                'countsupport11' : i[96],
                'totalsupport11' : i[97],
                'countdefend11' : i[98],
                'strength12' : i[99],
                'notorietyratio12' : i[100],
                'totalextort12' : i[101],
                'countextort12' : i[102],
                'countbenefit12' : i[103],
                'countpunish12' : i[104],
                'countsupport12' : i[105],
                'totalsupport12' : i[106],
                'countdefend12' : i[107],
                'strength13' : i[108],
                'notorietyratio13' : i[109],
                'totalextort13' : i[110],
                'countextort13' : i[111],
                'countbenefit13' : i[112],
                'countpunish13' : i[113],
                'countsupport13' : i[114],
                'totalsupport13' : i[115],
                'countdefend13' : i[116],
                'strength14' : i[117],
                'notorietyratio14' : i[118],
                'totalextort14' : i[119],
                'countextort14' : i[120],
                'countbenefit14' : i[121],
                'countpunish14' : i[122],
                'countsupport14' : i[123],
                'totalsupport14' : i[124],
                'countdefend14' : i[125],
                'strength15' : i[126],
                'notorietyratio15' : i[127],
                'totalextort15' : i[128],
                'countextort15' : i[129],
                'countbenefit15' : i[130],
                'countpunish15' : i[131],
                'countsupport15' : i[132],
                'totalsupport15' : i[133],
                'countdefend15' : i[134],
                'community1m1' : i[135],
                'community2m1' : i[136],
                'community3m1' : i[137],
                'community4m1' : i[138],
                'community5m1' : i[139],
                'community6m1' : i[140],
                'community7m1' : i[141],
                'community8m1' : i[142],
                'community9m1' : i[143],
                'community10m1' : i[144],
                'community11m1' : i[145],
                'community12m1' : i[146],
                'community13m1' : i[147],
                'community14m1' : i[148],
                'community15m1' : i[149],
                'community1m2' : i[150],
                'community2m2' : i[151],
                'community3m2' : i[152],
                'community4m2' : i[153],
                'community5m2' : i[154],
                'community6m2' : i[155],
                'community7m2' : i[156],
                'community8m2' : i[157],
                'community9m2' : i[158],
                'community10m2' : i[159],
                'community11m2' : i[160],
                'community12m2' : i[161],
                'community13m2' : i[162],
                'community14m2' : i[163],
                'community15m2' : i[164],
                'community1m3' : i[165],
                'community2m3' : i[166],
                'community3m3' : i[167],
                'community4m3' : i[168],
                'community5m3' : i[169],
                'community6m3' : i[170],
                'community7m3' : i[171],
                'community8m3' : i[172],
                'community9m3' : i[173],
                'community10m3' : i[174],
                'community11m3' : i[175],
                'community12m3' : i[176],
                'community13m3' : i[177],
                'community14m3' : i[178],
                'community15m3' : i[179],
                'community1m4' : i[180],
                'community2m4' : i[181],
                'community3m4' : i[182],
                'community4m4' : i[183],
                'community5m4' : i[184],
                'community6m4' : i[185],
                'community7m4' : i[186],
                'community8m4' : i[187],
                'community9m4' : i[188],
                'community10m4' : i[189],
                'community11m4' : i[190],
                'community12m4' : i[191],
                'community13m4' : i[192],
                'community14m4' : i[193],
                'community15m4' : i[194],
                'community1m5' : i[195],
                'community2m5' : i[196],
                'community3m5' : i[197],
                'community4m5' : i[198],
                'community5m5' : i[199],
                'community6m5' : i[200],
                'community7m5' : i[201],
                'community8m5' : i[202],
                'community9m5' : i[203],
                'community10m5' : i[204],
                'community11m5' : i[205],
                'community12m5' : i[206],
                'community13m5' : i[207],
                'community14m5' : i[208],
                'community15m5' : i[209],
                'community1m6' : i[210],
                'community2m6' : i[211],
                'community3m6' : i[212],
                'community4m6' : i[213],
                'community5m6' : i[214],
                'community6m6' : i[215],
                'community7m6' : i[216],
                'community8m6' : i[217],
                'community9m6' : i[218],
                'community10m6' : i[219],
                'community11m6' : i[220],
                'community12m6' : i[221],
                'community13m6' : i[222],
                'community14m6' : i[223],
                'community15m6' : i[224],
                'community1m7' : i[225],
                'community2m7' : i[226],
                'community3m7' : i[227],
                'community4m7' : i[228],
                'community5m7' : i[229],
                'community6m7' : i[230],
                'community7m7' : i[231],
                'community8m7' : i[232],
                'community9m7' : i[233],
                'community10m7' : i[234],
                'community11m7' : i[235],
                'community12m7' : i[236],
                'community13m7' : i[237],
                'community14m7' : i[238],
                'community15m7' : i[239],
                'community1m8' : i[240],
                'community2m8' : i[241],
                'community3m8' : i[242],
                'community4m8' : i[243],
                'community5m8' : i[244],
                'community6m8' : i[245],
                'community7m8' : i[246],
                'community8m8' : i[247],
                'community9m8' : i[248]
            })
            s.add(record) #Add all the records

        s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
