cat("Calculate the average \n")
cat("\n")

data <- data.frame (
  ids= c("bbaf8eec", "0242ac12", "bc12000"),
  subjects = c("Math", "English", "Science"),
  hrs_total = c(80, 60, 80),
  hrs_absent = c(23, 10, 22)
)

data$result <- (data$hrs_absent / data$hrs_total) * 100

print(data)
cat("\n")
cat("\n")
cat("Result:")
cat("\n")
print(data[["result"]])
