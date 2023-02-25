# %% -- import modules
from itertools import combinations

import numpy as np
import pandas as pd
import statsmodels.api as sm


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


# %% -- plots
(star_is_born
 .plot.scatter(x='talent', y='beauty', title='All people'))

# %%
(star_is_born[star_is_born.star == 1]
 .plot.scatter(x='talent', y='beauty', title='Stars'))

# %%
(star_is_born[star_is_born.star == 0]
 .plot.scatter(x='talent', y='beauty', title='Other people'))
