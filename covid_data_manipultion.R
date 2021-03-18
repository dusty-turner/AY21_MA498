library(tidyverse)

library(tidyverse)
library(readxl)

week1 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 1)%>% 
  janitor::clean_names()%>% filter(company != "NA")
week2 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 2) %>% 
  janitor::clean_names() 
week3 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 3) %>% 
  janitor::clean_names() 
week4 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 4) %>% 
  janitor::clean_names() 
week5 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 5) %>% 
  janitor::clean_names() 
week6 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 6) %>% 
  janitor::clean_names() 
week7 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 7) %>% 
  janitor::clean_names() 
week8 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 8) %>% 
  janitor::clean_names() 
week9 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 9) %>% 
  janitor::clean_names() 
week10 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 10) %>% 
  janitor::clean_names() 
week11 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 11) %>% 
  janitor::clean_names() 
week12 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 12) %>% 
  janitor::clean_names() 
week13 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 13) %>% 
  janitor::clean_names() 
week14 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 14) %>% 
  janitor::clean_names() 
week15 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 15) %>% 
  janitor::clean_names() 
week16 <- read_excel("testing_out_with_company_clean.xlsx", sheet = 16) %>% 
  janitor::clean_names()
  
week9 <- week9 %>% 
  # select(test_date, result, company, inc_prob) %>% 
  group_by(test_date, company) %>% 
  mutate(post_today_comp = max(result)) %>% 
  group_by(company) %>% 
  mutate(id_these_people_comp = cummax(post_today_comp)) %>% 
  # filter(id_these_people_comp==1) %>%
  group_by(test_date, result, post_today_comp, company) %>% 
  mutate(new_prob_comp = ifelse(post_today_comp == 0 & id_these_people_comp == 1, 
                                n()/122, inc_prob)) %>% 
  group_by(test_date, corps_squad) %>% 
  mutate(post_today_corps = max(result)) %>% 
  group_by(corps_squad) %>% 
  mutate(id_these_people_corps = cummax(post_today_corps)) %>% 
  # filter(id_these_people_comp==1) %>%
  group_by(test_date, result, post_today_corps, corps_squad) %>% 
  mutate(new_prob_corps = ifelse(post_today_corps == 0 & id_these_people_corps == 1,
                                 n()/37, inc_prob)) %>%
  mutate(new_prob_corps = ifelse(corps_squad=="NA", new_prob_comp, new_prob_corps)) %>% 
  select(inc_prob,new_prob_comp,new_prob_corps, id_these_people_comp) %>% 
  # filter(result  == 1)
  filter(id_these_people_comp == 1) %>% 
  rowwise() %>% 
  mutate(inc_prob = max(inc_prob, new_prob_comp, new_prob_corps) )

week16 <- week16 %>%
  mutate(ht_estimator = result * (1/inc_prob),
         ht_variance1 = ((result * inc_prob * inc_prob^2)/inc_prob^2))


week1 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1))
week2 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week3 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week4 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week5 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week6 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week7 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week8 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week9 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week10 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week11 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week12 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week13 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week14 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week15 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)
week16 %>% summarise(ht_estimator = (1/4392)*sum(ht_estimator),
                    ht_variance = ((1/4392)^2)*sum(ht_variance1)) %>%
  as_tibble() %>% arrange(-ht_estimator) %>% head(3)


#Attempt at adjusting for independence
#week1 <- week1 %>%
#  group_by(corps_squad, competetive_club) %>%
#  mutate(ht_variance2 = ((851/77400)-(sum(inc_prob) - inc_prob)*inc_prob))/
#  (851/77400)*(sum(inc_prob) - inc_prob)*inc_prob))
