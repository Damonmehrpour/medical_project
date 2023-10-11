import pandas as pd
import operator 
import os
os.system("cls")

tsmoke=1
twork=1
path='C:/Users/aweso/OneDrive/Desktop/medical project'
df = pd.read_csv(path+'/Book1.csv')
df=df.dropna()
length=int(df.shape[0])
#heart=df[operator.and_(df['History of Heart Failure']=='Yes',operator.and_ (df['Age']>40,))]
qw=df.sort_values(by=["Age"],ascending=False)
#dfsmoke=df.sort_values(by=["status of smoking"])[:length//2]
dfoxygen=df[df["Oxygen Saturation"]<=95]
dfrespirate=df[df["Respiratory Rate"]>=20]
#dfrespirate=df.sort_values(by=["Respiratory Rate"],ascending=False)[:length//2]      #beine 12 ta 19 normal az 20 be bala kheili khatarnak
dfsmoke=df[df["status of smoking"]==1]
#dfoxygen=df.sort_values(by=["Oxygen Saturation"])[:length//2]         #harchi kamtar badtar zire 96
dfbp=df[df["Blood pressure"]=="Crisis"]


or_df = pd.merge(dfoxygen, dfrespirate, how ='inner',left_index=True,right_index=True, suffixes=('', '_remove'))
or_df.drop([i for i in or_df.columns if 'remove' in i],axis=1, inplace=True)

bpsdf = pd.merge(dfbp, dfsmoke, how ='inner',left_index=True,right_index=True, suffixes=('', '_remove'))
bpsdf.drop([i for i in bpsdf.columns if 'remove' in i],axis=1, inplace=True)

result_df = pd.merge(bpsdf, or_df, how ='inner',left_index=True,right_index=True, suffixes=('', '_remove'))
result_df.drop([i for i in result_df.columns if 'remove' in i],axis=1, inplace=True)
count_int_df=result_df.shape[0]
print("First phase (Hospital refferal)")
print(dfrespirate)
print(dfoxygen)
print(dfsmoke)
print("Second phase(Primary care)")
print(result_df)
