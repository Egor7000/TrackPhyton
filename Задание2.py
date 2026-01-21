# Дано
disk_size_mb = 1.44  # Мб
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Перевод объёма дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Объём одной книги в байтах
book_size = pages * lines_per_page * chars_per_line * bytes_per_char

# Количество книг
books_count = int(disk_size_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books_count)
