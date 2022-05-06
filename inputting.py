def replacing_(text, args_dicts):
    """ this fuction take slang.txt dict and 
    replace all contracted slang
    
    Arg: 
    args_dict : dicitionary
    
    return : full string ex. iso a car -> in search of a car """
    for key in args_dict.keys():
        text = str(text).replace(key, str(args_dict[key]))
    return text

    # Strongly Recomend to use with pandas 
    #pd[col] = pd[col].apply(lambda row , replacing_(row, dict))