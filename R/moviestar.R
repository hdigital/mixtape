library(tidyverse)

set.seed(3444)


## Create dataset ----

star_is_born <- tibble(
  beauty = rnorm(2500),
  talent = rnorm(2500),
  score = beauty + talent,
  star = ifelse(quantile(score, 0.85) >= score, 1, 0)
)


## Plot data ----

plot_data <- function(dt) {
  ggplot(dt, aes(x = talent, y = beauty)) +
    geom_point(size = 0.5, shape = 23) + 
    xlim(-4, 4) + 
    ylim(-4, 4)
}


plot_data(star_is_born)

star_is_born |>
  filter(star == 1) |>
  plot_data()

star_is_born |> 
  filter(star == 0) |>
  plot_data()
