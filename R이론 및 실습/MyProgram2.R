
ids = 1:100
name_list = paste('name-', ids, sep='')
age_list = sample(10:70,100,replace = TRUE)
income_list = sample(1:100, 100, replace = TRUE) * 100

book = data.frame(id=ids, name=name_list, 
                  age=age_list, income=income_list)
