import pandas as pd
technologies= ({
    'Courses':["Spark","PySpark","Hadoop","Pandas","Spark","PySpark", "Pandas"],
    'Fee': [22000,25000,30000,35000,22000,25000,35000],
    'Duration':['30days','50days','40days','35days','30days','50days','60days'],
    'Discount':[1000,2000,2500,1500,1000,2000,1500]
              })
index_labels=['r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=index_labels)
print(df)
# Get value from DataFrame column
print(df.loc[df.Duration == '40days','Duration'].values[0])