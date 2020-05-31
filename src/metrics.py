import numpy as np

def precision(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
    
    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
        
    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
        
    # your_code
    # Лучше считать через скалярное произведение, а не цикл
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    recommended_top_prise = prices_recommended[:k]
    
    # создаем пустой список длинной k элементов
    flags = [0] * k
    
    # зпаолняем единицамми, в зависимости от совпадений покупок и рекомендаций
    for i, v in enumerate(recommended_top[:k]):
        if v in bought_list:
            flags[i] = 1
    
    precision = (flags @ recommended_top_prise) / recommended_top_prise.sum()

    return precision


def recall_at_k(recommended_list, bought_list, k=5):
    
    # your_code
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list[:k])
    
    recall = flags.sum() / len(bought_list)
    
    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    
    # your_code
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    prices_bought = np.array(prices_bought)
    recommended_top_prise = prices_recommended[:k]
    
    # создаем пустой список длинной k элементов
    flags = [0] * k
    
    # зпаолняем единицамми, в зависимости от совпадений покупок и рекоммендаций
    for i, v in enumerate(recommended_top[:k]):
        if v in bought_list:
            flags[i] = 1
            
    recall = (flags @ recommended_top_prise) / prices_bought.sum()
    
    return recall

