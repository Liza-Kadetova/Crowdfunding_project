vec <- seq(-3, 3, 0.01)
plot(vec, dnorm(vec))
dnorm(vec, mean = 100, sd = 15) #нормальное распределение
iq <- seq(50, 150, 0.1) 
plot(iq, pnorm(iq, 100, 15))
pnorm(100, mean = 100, sd = 15)  #кумулятивное распределние
pnorm(130, mean = 100, sd = 15) 
qnorm(0.25, mean = 100, sd = 15) #из вероятности дает, сколько в выборке проявлений
samp <- rnorm(100, mean = 100, sd = 15) #случайные сто экз из выборки
? rnorm
set.seed(42)
hist(samp)
mean(samp)
? Distributions
x <- seq(20000,200000,1000)
q <- seq(20000,200000,1000)
dlnorm(x, meanlog = 0, sdlog = 1, log = FALSE)
plnorm(q, meanlog = 0, sdlog = 1, lower.tail = TRUE, log.p = FALSE)
qlnorm(p, meanlog = 0, sdlog = 1, lower.tail = TRUE, log.p = FALSE)
rlnorm(n, meanlog = 0, sdlog = 1)
means <- replicate(10000, mean(rnorm(100, mean = 100, sd = 15)))
hist(means)
m <- mean(samp)
se <-  function(x) sd(samp)/sqrt(length(x))
sem <- se(samp)
m + sem #доверительный интервал
m - sem
qnorm(0.975)
zcr <- qnorm(1 - (1-0.95)/))

samp2 <- qnorm(0.5, mean = 100, sd = 15)
length(samp2)

#формулирование гипотезы
#подсчет тестовой статистики
#подсчет p-value (не может быть больше 1)
#принятие решение (сравниваем p-value с альфа (0,05) если меньше отвергаем нулевую гипотезу
# если больше, то принимаем)

z <- (m - 100)/(15/10) #pvalue 
z 
#распределение зет-статистик
pnorm(z)
(1 - pnorm(z)) * 2 #при верности нулевой гипотезы это вероятность получить такое и более отклоняющееся среднее
#p-value это коэфф удивления :)) он говорит, что при верность НГ вероятность получить это значегие вот  такое
# но при том ничего не говорит о ненулевой гипотезе


