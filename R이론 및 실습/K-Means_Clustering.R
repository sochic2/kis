num_of_clusters=5
num_of_elements=200

x = sample(1:1000, num_of_elements, replace=F)
y = sample(1:1000, num_of_elements, replace=F)

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


