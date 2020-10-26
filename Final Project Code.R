#Final Project Code
#Ben Lambright

#You will work to identify which notes identify patients who have diabetic complications of neuropathy, nephropathy, 
#and/or retinopathy and which type of complication the note identifies.


#importing necessary packages
library(tidyverse)
library(magrittr)
library(bigrquery)

con <- DBI::dbConnect(drv = bigquery(),
                      project = "learnclinicaldatascience")
diabetes_notes <- tbl(con, "course4_data.diabetes_notes") %>% 
  collect()

#I decided to use the keyword window approach
#the following is a function to create a keyword window (obtained from a previous class)
extract_text_window <- function(dataframe, keyword, half_window_size) {
  dataframe %>% 
    group_by(NOTE_ID) %>% 
    mutate(WORDS = TEXT) %>% 
    separate_rows(WORDS, sep = "[ \n]+") %>% 
    mutate(INDEX = seq(from = 1, to = n(), by = 1.0),
           WINDOW_START = case_when(INDEX - half_window_size < 1 ~ 1,
                                    TRUE ~ INDEX - half_window_size),
           WINDOW_END = case_when(INDEX + half_window_size > max(INDEX) ~ max(INDEX),
                                  TRUE ~ INDEX + half_window_size),
           WINDOW = word(string = TEXT, start = WINDOW_START, end = WINDOW_END, sep = "[ \n]+")) %>% 
    ungroup() %>% 
    filter(str_detect(string = WORDS, pattern = regex(keyword, ignore_case = TRUE)))
}

#my dataframe is diabetes_notes, keyword will be the regex "(?<![a-zA-Z])(neuropathy|nephropathy|retinopathy)(?![a-zA-z])", and window size will be 8 (I'm only searching for negation)
#definted variable as finding so I could look at it on another tab
findings <- diabetes_notes %>%
  extract_text_window(keyword = "(?<![a-zA-Z])(neuropathy|nephropathy|retinopathy)(?![a-zA-z])", half_window_size = 8) %>%d
  mutate(EXCLUDE = case_when(str_detect(WINDOW, regex(pattern = "no (neuropathy|nephropathy|retinopathy)", ignore_case = TRUE)) ~ 1,
                           TRUE ~ 0)) %>%
  filter(EXCLUDE != 1)
#findings

#finding all of the notes which had the keyword (making sure there are no repeats)
distinct_notes <- findings %>%
  distinct(NOTE_ID)
distinct_notes

#remember 21 & 51 for presentation
