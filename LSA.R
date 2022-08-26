install.packages("LSAfun")
library(LSAfun)

# remove.packages("rgl")
install.packages("rgl", dependencies = TRUE)

setwd("/Users/deekshavyas/Documents/Dissertation/sem2/CodeTesting/json_to_csv/All_combined_Irish_docs")
install.packages("lsa")
library("lsa")
z = textmatrix("./")
l = lsa(z)
neighbors("activeageing",n=20,tvectors = l$tk)

plot_neighbors("activeageing",n=20,tvectors = l$tk)

l = lsa(z, 2)
write.table(l$tk,file="../Matrix_Data/tokenFile.txt", sep = ",")
l = lsa(z, 5)
write.table(l$tk,file="../Matrix_Data/tokenFile2.txt", sep = ",")

D <- read.csv("../Matrix_Data/tokenFile2_em_wtype.csv",header=TRUE,stringsAsFactors=TRUE)
summary(D)

with(D,tapply(V1,list(emotion),mean))
with(D,tapply(V2,list(emotion),mean))
with(D,tapply(V3,list(emotion),mean))
with(D,tapply(V4,list(emotion),mean))
with(D,tapply(V5,list(emotion),mean))

with(D,tapply(V1,list(word_type),mean))
with(D,tapply(V2,list(word_type),mean))
with(D,tapply(V3,list(word_type),mean))
with(D,tapply(V4,list(word_type),mean))
with(D,tapply(V5,list(word_type),mean))

with(D,shapiro.test(V1))
with(D,shapiro.test(V2))
with(D,shapiro.test(V3))
with(D,shapiro.test(V4))
with(D,shapiro.test(V5))

with(D, kruskal.test(V1~emotion))
with(D, kruskal.test(V2~emotion))
with(D, kruskal.test(V3~emotion))
with(D, kruskal.test(V4~emotion))
with(D, kruskal.test(V5~emotion))

with(D,kruskal.test(V1~word_type))
with(D,kruskal.test(V2~word_type))
with(D,kruskal.test(V3~word_type))
with(D,kruskal.test(V4~word_type))
with(D,kruskal.test(V5~word_type))

with(D,tapply(V1,list(word_type,emotion),mean))
with(D,tapply(V2,list(word_type,emotion),mean))
with(D,tapply(V3,list(word_type,emotion),mean))
with(D,tapply(V4,list(word_type,emotion),mean))
with(D,tapply(V5,list(word_type,emotion),mean))

with(D,interaction.plot(word_type,emotion,V1))
with(D,interaction.plot(word_type,emotion,V2))
with(D,interaction.plot(word_type,emotion,V3))
with(D,interaction.plot(word_type,emotion,V4))
with(D,interaction.plot(word_type,emotion,V5))

plot_neighbors("limerick",n=20,tvectors = l$tk)
plot_neighbors("limerick",n=20,tvectors = q$tk)
plot_neighbors("limerick",n=20,tvectors = q$tk)
plot_neighbors("learning",n=20,tvectors = q$tk)
plot_neighbors("learning",n=20,tvectors = q$tk)
plot_neighbors("new",n=20,tvectors = q$tk)
plot_neighbors("lifelong",n=20,tvectors = q$tk)
plot_neighbors("limerick",n=20,tvectors = l$tk)
plot_neighbors("elder",n=20,tvectors = l$tk)
plot_neighbors("elder",n=20,tvectors = q$tk)
plot_neighbors("elderly",n=20,tvectors = q$tk)
summary(q)
q$tk
l$tk



