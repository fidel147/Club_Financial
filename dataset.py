from settings import *

class ClubFinancials:

    def __init__(self, data, **indexing):
        self.data = data['club_financials']
        self.__indexing = indexing

    @property
    def indexing(self):
        return self.__indexing

    @indexing.setter
    def indexing(self, value):
        if not isinstance(value, dict):
            raise ValueError("Indexing must be a dictionary.")
        self.__indexing.update(value)
    
    def get_club(self):
        filtered = self.data[self.data["club_name"] == self.__indexing['club_name']]
        filtered = filtered.sort_values('year').reset_index(drop=True)
        return filtered

    def __groupby(self, *args):
        return self.get_club().groupby(*args)
    
    #calculate the revenue growth rate
    def revenue_growth_rate(self):

        #revenue growth rate
        year2010 = self.get_club()[self.get_club()['year'] == 2010]
        year2026 = self.get_club()[self.get_club()['year'] == 2026]
        revenue2010 = year2010['revenue_eur_m'].mean()
        revenue2026 = year2026['revenue_eur_m'].mean()
        growth_rate = ((revenue2026 - revenue2010) / revenue2010)

        #gagr 
        gagr = (revenue2026 / revenue2010) ** (1 / (2026 - 2010)) - 1
        return growth_rate, gagr

    def __metrics_elif(self, metrics, groupby_year):
        if set(metrics).issubset(set(self.get_club().columns)):
                            n = len(metrics)
                            ncols = 2
                            nrows = math.ceil(n / ncols)
                            fig, axes = plt.subplots(nrows, ncols, figsize=(14, 5*nrows))
        
                            for ax, metric in zip(axes.flatten(), metrics):
                                groupby_year[metric].sum().plot(kind='bar', ax=ax, title=metric.replace("_", " ").title())
                                ax.tick_params(axis='x', rotation=45)
        
                            for ax in axes.flatten()[n:]:
                                ax.axis('off')
        
                            plt.tight_layout(pad=10.0)
                            plt.show()
    def plot_revenue(self, *metrics):
        groupby_year = self.__groupby('year')
        if len(metrics) != 0:
            if len(metrics) == 1:
                groupby_year[metrics[0]].sum().plot(kind='bar', title=metrics[0].replace("_", " ").title())
                plt.show()
            elif len(metrics) > 1:
                self.__metrics_elif(metrics, groupby_year)
            else:
                missing_metrics = set(metrics) - set(self.get_club().columns)
                raise ValueError(f"Metrics {missing_metrics} not found in the dataset.")
    def plot_tendancy(self, columns):
         groupby_year = self.__groupby('year')
         if columns not in self.get_club().columns:
             raise ValueError(f"Column {columns} not found in the dataset.")
         else:
            groupby_year[columns].sum().plot(kind="line", title=columns.replace("_", " ").title())
            plt.xticks(rotation=45)
            plt.show()

    def correff(self, X=None, Y=None):
         groupby_year = self.__groupby('year')
         if X is None or Y is None:
             raise ValueError("Both X and Y must be provided.")
         elif X not in self.get_club().columns or Y not in self.get_club().columns:
             raise ValueError(f"Columns {X} and/or {Y} not found in the dataset.")
         else:
              correff = np.corrcoef(groupby_year[X].sum(), groupby_year[Y].sum())[0, 1]
              return correff

    def double_ax(self, *metrics):
         groupby_year = self.__groupby('year')
         if len(metrics) != 2:
             raise ValueError("Exactly two metrics must be provided for double axis plotting.")
         elif not set(metrics).issubset(set(self.get_club().columns)):
             missing_metrics = set(metrics) - set(self.get_club().columns)
             raise ValueError(f"Metrics {missing_metrics} not found in the dataset.")
         else:
                fig, ax1 = plt.subplots(figsize=(10, 6))
                color1 = 'tab:blue'
                ax1.set_xlabel('Year')
                ax1.set_ylabel(metrics[0].replace("_", " ").title(), color=color1)
                groupby_year[metrics[0]].sum().plot(kind='bar', ax=ax1, color=color1)
                ax1.tick_params(axis='y', labelcolor=color1)

                ax2 = ax1.twinx()
                color2 = 'tab:red'
                ax2.set_ylabel(metrics[1].replace("_", " ").title(), color=color2)
                groupby_year[metrics[1]].sum().reset_index(drop=True).plot(kind='line', ax=ax2, color=color2)
                ax2.tick_params(axis='y', labelcolor=color2)

                plt.title(f"{metrics[0].replace('_', ' ').title()} and {metrics[1].replace('_', ' ').title()} Over Years")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

class LigueComparison(ClubFinancials):
    def __init__(self, data, **indexing):
        super().__init__(data, **indexing)