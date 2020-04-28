library(rpart)
View(kyphosis)

fit = rpart(Kyphosis ~ Age + Number + Start, 
            method = "class", data=kyphosis)           

plot(fit, uniform=TRUE, 
     main = "Classification Tree for kyphosis") 

text(fit, use.n=TRUE, all=TRUE, cex=.5)
