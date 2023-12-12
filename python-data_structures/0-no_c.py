def no_c(my_string):
    lower= my_string.lower()
    return lower.translate({ord("c"): ""})
        
        
print(no_c())