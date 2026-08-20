from pathlib import Path

import streamlit as st

from utils.data_loader import load_data


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@st.cache_data
def load_superstore_data():
	csv_candidates = (
		DATA_DIR / "Sample - Superstore.xlsx - Orders.csv",
		DATA_DIR / "sample_superstore.csv",
	)
	for csv_path in csv_candidates:
		if csv_path.exists():
			return load_data(str(csv_path))
	raise FileNotFoundError("Superstore CSV dataset was not found")


def get_filtered_data(df, filters):
	from utils.filters import apply_filters

	return apply_filters(df, filters)


def display_metrics(df, metrics):
	columns = st.columns(4)
	columns[0].metric("Total Sales", f"${metrics['total_sales']:,.0f}")
	columns[1].metric("Total Profit", f"${metrics['total_profit']:,.0f}")
	columns[2].metric("Total Orders", f"{metrics['total_orders']:,}")
	columns[3].metric("Total Customers", f"{metrics['total_customers']:,}")


def empty_state():
	st.info("No data is available for the selected filters.")
