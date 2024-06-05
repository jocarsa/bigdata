library(ggplot2)

data <- read.csv("C:/Users/Admin/Documents/GitHub/bigdata/007-Flujo con R/visitasmensuales.csv")

# Convert the date column to a Date object
data$mes <- as.Date(paste0(data$mes, "-01"))

# Create the plot
ggplot(data, aes(x = mes, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(x = "Month", y = "Visitor Count", title = "Visitor Count per Month")