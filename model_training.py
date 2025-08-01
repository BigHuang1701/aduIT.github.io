import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Đọc file CSV đã tải lên
df = pd.read_csv('/content/consumer_electronics_sales_data.csv')
df.head()

# Chọn các cột đầu vào (features) và đầu ra (label)
features = ['ProductPrice', 'CustomerAge', 'PurchaseFrequency', 'CustomerSatisfaction']
target = 'PurchaseIntent'

# X và y
X = df[features]
y = df[target]

# Chia thành tập huấn luyện và kiểm tra (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df.info()
df.describe()

df.isnull().sum()
df.duplicated().sum()

# Xoá các dòng bị thiếu
df.dropna(inplace=True)

# Xoá dữ liệu trùng
df.drop_duplicates(inplace=True)

df['Sales'] = df['ProductPrice'] * df['PurchaseFrequency']

category_sales = df.groupby('ProductCategory')['Sales'].sum().reset_index()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.countplot(x='CustomerSatisfaction', data=df)
plt.title('Distribution of Satisfaction Level')
plt.xlabel('Satisfaction Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.boxplot(x='CustomerSatisfaction', y='CustomerAge', data=df)
plt.title('Age vs Satisfaction')
plt.xlabel('Satisfaction Level')
plt.ylabel('Customer Age')
plt.show()

sns.boxplot(x='CustomerSatisfaction', y='PurchaseFrequency', data=df)
plt.title('Purchase Frequency vs Satisfaction')
plt.xlabel('Satisfaction Level')
plt.ylabel('Purchase Frequency')
plt.show()

plt.scatter(df['ProductPrice'], df['CustomerSatisfaction'])
plt.title('Product Price vs Satisfaction')
plt.xlabel('Product Price')
plt.ylabel('Satisfaction Level')
plt.show()

numeric_df = df.select_dtypes(include=np.number)
sns.heatmap(numeric_df.corr(), annot=True, cmap='Blues')
plt.title('Correlation Heatmap')

# Khởi tạo model
model = LinearRegression()

# Huấn luyện
model.fit(X_train, y_train)

# Dự đoán trên tập test
y_pred = model.predict(X_test)

# Đánh giá
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R²):", r2)

# So sánh thực tế và dự đoán
comparison = pd.DataFrame({'Thực tế': y_test.values, 'Dự đoán': y_pred})
print(comparison.head(10))

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Satisfaction Level')
plt.ylabel('Predicted Satisfaction Level')
plt.title('Actual vs Predicted Satisfaction')
