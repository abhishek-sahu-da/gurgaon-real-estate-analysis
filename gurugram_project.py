import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


df=pd.read_csv('gurugram.csv' )

df=df.drop_duplicates()
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print(df.columns.to_list())
# #converting dtype
df['price']=df['price'].astype(str).str.replace(",", "").astype(float)
df['area']=df['area'].astype(str).str.replace(",", "").astype(float)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(",", "").astype(float)
df['area']=df['area'].astype(float)
# print(df[['price','area','rate_per_sqft']])

#categorical columns cleaning 
df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approved by rera':True ,'not approved by rera':False})
df['flat_type']=df['flat_type'].str.strip().str.lower()

# print(df['flat_type'])
df=df.drop_duplicates()
costliest_flat = df.sort_values('price', ascending=False).iloc[0]
# print(costliest_flat)
print(f'the costliest flat is in  {costliest_flat['locality']} and costs {costliest_flat['price']/10000000}cr.')

print(df.groupby('locality')['price'].agg(['mean','count']).sort_values('mean',ascending=False).head(5))
print(df.groupby('locality')['rate_per_sqft'].agg(['mean']).sort_values('mean',ascending=False).head(5))
print(df.groupby('status')[['price','rate_per_sqft']].mean())
print(df.groupby('rera_approval')['price'].mean())
rera_approved_avg= df[df['rera_approval']==True]['price'].mean()
not_rera_approved_avg= df[df['rera_approval']==False]['price'].mean()

if rera_approved_avg> not_rera_approved_avg:
     print('rera approved charges premium ')
else:
     print('rera approved dont charge price preminum ')


print(df['area'].corr(df['price'], method='spearman'))
# sns.scatterplot(data=df,x='area',y='price')
# plt.show()
print(df.groupby('bhk_count')['rate_per_sqft'].mean().sort_values(ascending=False).idxmax())

print(df.groupby('flat_type')['price'].mean().sort_values(ascending=False))
print(df.groupby('builder_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))
# sns.scatterplot(data = df , x='area', y = 'rate_per_sqft')
# plt.show()

print(df['locality'].value_counts().head(5)) 
print(df.groupby('flat_type')['area'].mean().sort_values(ascending=False))
print(df['rera_approval'].value_counts())
print(df.groupby('locality')['price'].agg(['mean', 'count']).query('count>=20').sort_values('mean',ascending=True).head(1))

avgp_3bhk = df[(df['bhk_count'] == 3) & (df['flat_type'] == 'apartment')]['price'].mean()
print(f'average price of 3 bhk apartments is {avgp_3bhk / 10000000:.2f} cr.') 
print()
avg_2bhk= df[(df['bhk_count'] == 2)]['price'].mean()
print(f'avg price for 2 bhk plot is {avg_2bhk:.2f}')
print(df.groupby(['status','rera_approval'])['rate_per_sqft'].mean())
print(df['company_name'].value_counts().head(5))
df['price_crores']=df['price']/10000000
print(df['price_crores'])
count = (df['price'] > 100000000).sum()
print(count)
result=df[(df['bhk_count']==3 )& (df['flat_type']=='apartment')].groupby('locality')['price'].agg(['mean', 'count']).query('count>=10').sort_values('mean',ascending= False   )
print(result)
# df['locality'].value_counts().head(10).plot(kind='bar')
# plt.title('top 10 localities by listing ')
# plt.xlabel('localities')
# plt.ylabel('listing')
# sns.histplot(data=df[df['rate_per_sqft']<50000], x='rate_per_sqft',bins=30)
# plt.title('distribution of rate per sqft ')
# plt.show()
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='flat_type', y='price')
plt.title("Price by Flat Type")
plt.show()