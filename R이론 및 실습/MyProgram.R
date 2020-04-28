#book = NULL
load('book.RData')
while(TRUE) {

  name = readline('Name:')
  
  if(name=='s') { break }
  
  age = readline('Age:')
  income = readline('Income:')
  age = as.numeric(age)
  income = as.numeric(income)
  new_item = data.frame(name=name, age=age,income=income)  
  
  if(is.null(book)){
    book = new_item
  } else {
    book = rbind(book, new_item)
  }
  
  save(book, file='book.RData')
  print(book)

}





