def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

if __name__ == "__main__":
    stock_price = [14,20,4,12,5,11]
    print(buy_and_sell(stock_price))