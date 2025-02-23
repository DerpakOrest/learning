# ✅ Імпорт бібліотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------
# 📊 1. СТВОРЕННЯ DATAFRAME (Власний набір даних)
# ----------------------------------------------
data = pd.DataFrame({
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Headphones'],
    'Price': [1200, 800, 400, 300, 50, 40, 200, 150],
    'Units Sold': [150, 250, 180, 120, 300, 350, 90, 200]
})

# Вивід DataFrame
print("📋 DataFrame:")
print(data)

# ----------------------------------------------
# 📏 2. ОБЧИСЛЕННЯ СЕРЕДНІХ, МІНІМАЛЬНИХ ТА МАКСИМАЛЬНИХ ЗНАЧЕНЬ
# ----------------------------------------------
# Середнє значення
mean_price = data['Price'].mean()
mean_units = data['Units Sold'].mean()

# Мінімальне значення
min_price = data['Price'].min()
min_units = data['Units Sold'].min()

# Максимальне значення
max_price = data['Price'].max()
max_units = data['Units Sold'].max()

# Вивід результатів
print("\n📊 Середнє значення:")
print(f"💰 Середня ціна: {mean_price}")
print(f"📦 Середня кількість проданих одиниць: {mean_units}")

print("\n🔻 Мінімальні значення:")
print(f"💰 Мінімальна ціна: {min_price}")
print(f"📦 Мінімальна кількість проданих одиниць: {min_units}")

print("\n🔺 Максимальні значення:")
print(f"💰 Максимальна ціна: {max_price}")
print(f"📦 Максимальна кількість проданих одиниць: {max_units}")

# ----------------------------------------------
# 📈 3. ГРАФІК: ПОРІВНЯННЯ ДВОХ ПАРАМЕТРІВ (Новий стиль)
# ----------------------------------------------
plt.figure(figsize=(14, 7))
colors = plt.cm.Paired(np.linspace(0, 1, len(data['Product'])))

# 🟦 Стовпчаста діаграма для кількості продажів
bars = plt.bar(data['Product'], data['Units Sold'], color=colors, label='Units Sold', alpha=0.8)

# 🔴 Лінійний графік для цін
plt.plot(data['Product'], data['Price'], color='red', marker='D', linestyle='--', linewidth=2, label='Price ($)')

# 💡 Додав підписи на стовпцях
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height}', ha='center', fontsize=9)

# Заголовки та підписи
plt.title('💰 Порівняння Ціни та Продажів за Продуктами', fontsize=16)
plt.xlabel('Продукт', fontsize=12)
plt.ylabel('Значення', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ----------------------------------------------
# ➗ 4. ВИКОРИСТАННЯ NUMPY ДЛЯ МАТЕМАТИЧНИХ ОПЕРАЦІЙ
# ----------------------------------------------
# Перетворення стовпця "Ціна" в масив NumPy
price_array = np.array(data['Price'])

# Операції з NumPy
total_revenue = np.sum(price_array * data['Units Sold'])  # Загальний дохід
std_dev_price = np.std(price_array)  # Стандартне відхилення ціни
normalized_price = (price_array - np.mean(price_array)) / np.std(price_array)  # Нормалізація

# Вивід результатів
print("\n💵 Використання NumPy:")
print(f"💲 Загальний дохід: {total_revenue}")
print(f"📏 Стандартне відхилення ціни: {std_dev_price:.2f}")
print(f"📊 Нормалізовані значення ціни: {normalized_price}")
print("123456cl")