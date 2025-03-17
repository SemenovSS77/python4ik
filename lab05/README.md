# Задание 1
## Условия задания:
Генератор, применяющий заданную функцию к каждому элементу последовательности N раз.
Верните только те элементы, которые изменились значительно (зависит от N и типа данных).
## Проделанная работа:
Создали функцию apply_n_times, которая применяет func к value n раз. Каждый результат предыдущего 
вызова становится новым значением value.  
Сделали функцию filter_changed, которая фильтрует элементы последовательности seq, оставляя только те,
которые изменились значительно после применения func n раз.
Значительным изменением считается, если между новым и прошлым значением превышается порог threshold * abs(item).  
Добавили функцию square, которая возводит наше значение в квадрат.  
  
Вводим данные вручную numbers, n, threshold(разница).
Обявляем новую переменную result_generator, в которой храним filter_changed с нашими данными.  
Сделали переменную out_filter для фильтрации нашего result_generator с условием x > 15.  
Для удобства отсортировали out_filter в переменной sorted_result.  
![image](https://github.com/user-attachments/assets/fc249391-8561-4006-94c2-f7a1430b3336)

# Ссылки на материалы:
## [filter](https://timeweb.cloud/tutorials/python/kak-rabotaet-funkciya-filter-v-python?ysclid=m8db7fvtgo647604526)  
## [generator](https://skillbox.ru/media/code/generatory_python_chto_eto_takoe_i_zachem_oni_nuzhny/?ysclid=m8db706ebu363215932)
