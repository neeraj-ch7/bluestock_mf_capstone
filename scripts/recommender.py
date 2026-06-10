import pandas as pd

def recommend_funds(risk_appetite, df_scheme_performance, num_recommendations=3):
    recommender_data = df_scheme_performance[['amfi_code', 'scheme_name', 'risk_grade', 'sharpe_ratio']].copy()
    recommender_data.dropna(subset=['risk_grade', 'sharpe_ratio'], inplace=True)
    filtered_funds = recommender_data[recommender_data['risk_grade'].str.contains(risk_appetite, case=False, na=False)]
    if filtered_funds.empty:
        return pd.DataFrame()
    recommended = filtered_funds.sort_values(by='sharpe_ratio', ascending=False).head(num_recommendations)
    return recommended[['scheme_name', 'risk_grade', 'sharpe_ratio']]
