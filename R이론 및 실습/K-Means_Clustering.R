num_of_clusters=10
num_of_elements=20000

x = sample(1:1000, num_of_elements, replace=T)
y = sample(1:1000, num_of_elements, replace=T)

t_data = data.frame(x=x, y=y)

plot(x, y, cex=0.1)

res = kmeans(t_data, num_of_clusters)

for(i in 1:num_of_clusters) {
  
  for(j in which(res$cluster==i)){
    lines(c(res$centers[i,1], t_data[j,1]),
          c(res$centers[i,2], t_data[j,2]),
          col=i+3)
  }
  
  points(res$centers[i,1], res$centers[i, 2],
         col='red', cex=2)
  
  text(res$centers[i,1],res$centers[i,2],
       labels=paste('center-',i), pos=3,
       cex=0.7)
}


