# %% -- import modules
from itertools import combinations

import numpy as np
import pandas as pd
import statsmodels.api as sm
import plotnine as p9


# %% -- read data
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def read_data(file):
	return pd.read_stata("https://github.com/scunning1975/mixtape/raw/master/" + file)



# %% -- create dataset
star_is_born = pd.DataFrame(
	{
        'beauty': np.random.normal(size=2500),
        'talent': np.random.normal(size=2500)
    }
)

star_is_born['score'] = star_is_born['beauty'] + star_is_born['talent']
star_is_born['c85'] = np.percentile(star_is_born['score'], q=85)
star_is_born['star'] = 0
star_is_born.loc[star_is_born['score'] > star_is_born['c85'], 'star'] = 1
star_is_born.head()


# %% -- linear model // all people
lm_1 = sm.OLS.from_formula('beauty ~ talent', data=star_is_born).fit()
print(lm_1.summary())

# %% -- linear model // interaction effect
lm_2 = sm.OLS.from_formula('beauty ~ talent * star', data=star_is_born).fit()
print(lm_2.summary())


# %% -- plot

def plot_data(data, title = ""):
    plot = (
        p9.ggplot(data, p9.aes(x='talent', y='beauty')) +
            p9.geom_point(size=0.5) +
            p9.geom_smooth(method="lm", se=False, colour="blue") +
            p9.xlim(-4, 4) +
            p9.ylim(-4, 4) +
            p9.labs(title=title)
    )
    return plot

# %%
plot_data(star_is_born, "All people")
# %%
plot_data(star_is_born[star_is_born.star == 1], "Other people")
# %%
plot_data(star_is_born[star_is_born.star == 0], "Stars")
