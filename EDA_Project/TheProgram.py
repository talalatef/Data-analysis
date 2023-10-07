import pandas as pd 
import matplotlib.pyplot as plt 


def Read_data(data_path):
	type_data_file = input("Enter the Type of the file[excel, csv]:").lower()
	if type_data_file == 'excel':
		data = pd.read_excel(data_path)
	elif type_data_file == 'csv':
		data = pd.read_csv(data_path)
	else:
		print("this is not type the programe support.\n please enter acceptable file type.")
	return data

def Define_Columns_type(data):
	cols = data.columns
	numiric_cols = []
	categorical_cols = [] 
	
	for col in cols:
		if data[col].dtype == 'int64':
			numiric_cols.append(col)
		else:
			categorical_cols.append(col)
	return numiric_cols, categorical_cols

def Univariant_analysis(data):
	numiric_cols, categorical_cols = Define_Columns_type(data)
	numiric_data_frame = data[numiric_cols].copy()
	categorical_data_frame = data[categorical_cols].copy()
	Responce_1 = input('Do you want Univariant_analysis for numiric_data or categorical_data?[numiric_data, categorical_data]').lower()
	if Responce_1 == 'numiric_data':
		print(numiric_data_frame.describe().T)
	elif Responce_1 == 'categorical_data':
		print(categorical_data_frame.describe().T)
	else:
		print('Please Enter acceptable answer.')

def Univariant_Plots(data):
	numiric_cols, categorical_cols = Define_Columns_type(data)
	numiric_data_frame = data[numiric_cols].copy()
	categorical_data_frame = data[categorical_cols].copy()
	Responce_4 = True
	while Responce_4:
		Responce_1 = input('Do you want Univariant_Plots for numiric_data or categorical_data[numiric_data, categorical_data]:').lower()
		if Responce_1 == 'numiric_data':
			Responce_2 = input('there is three plots for numiric_data[histplot, boxplot, densityplot],\n What you want?')
			Responce_3 = input('Ok, give me the column you want to plot it:')
			if Responce_2 == 'histplot':
				data[Responce_3].plot.hist()
				# show plots 
				plt.show()
			elif Responce_2 == 'boxplot':
				data[Responce_3].plot.box()
				plt.show()
			elif Responce_2 == 'densityplot':
				data[Responce_3].plot.density()
				plt.show()
			else:
				print('please give me correct plot.')
		if Responce_1 == 'categorical_data':
			Responce_2 = input('there is one plot for categorical_data[bar_blot], Do you want do it[yes/no]?').lower()
			if Responce_2 == 'yes':
				Responce_3 = input('Ok, give me the column you want to plot it:')
				data[Responce_3].value_counts().plot.bar()
				# show plots 
				plt.show()
			elif Responce_2 == 'no':
				print("Ok.")
		Responce_5 = input("Do you want another plot?[yes,no]").lower()
		if Responce_5 == 'yes':
			Responce_4 = True
		else:
			Responce_4 = False


def Bivariant_analysis(data):
	numiric_cols, categorical_cols = Define_Columns_type(data)
	numiric_data_frame = data[numiric_cols].copy()
	categorical_data_frame = data[categorical_cols].copy()

	Responce_1 = input("Do you want to do Bivariant_analysis?[yes, no]:").lower()
	if Responce_1 == "yes":
		Responce_2 = input("Do you want to do Bivariant_analysis for numiric_data or categorical_data?[numiric_data, categorical_data]").lower()
		if Responce_2 == "numiric_data":
			print("This is Correlation for numiric_data to tell us the related cols.")
			print(numiric_data_frame.corr())
		if Responce_2 == "categorical_data":
			Responce_3 = input("There is pivot tabel for that purpose, give me the aggregate function you want to apply:")
			Responce_4 = input("give me the index column:")
			Responce_5 = input("give me the other column:")
			print(categorical_data_frame.pivot_table(index = Responce_4, values = Responce_5, aggfunc = Responce_3))







if __name__ == '__main__':
	# access my data
	DATA_PATH = input('Enter The Path Of Your Data:')
	my_data = Read_data(DATA_PATH)
	print(my_data.head())

	# define columns types

	responce_1 = input('Do you want to know the types of your columns?[yes/no]').lower()

	numiric_cols, categorical_cols = Define_Columns_type(my_data)

	if responce_1 == 'yes':
		print(f'Numiric columns:{numiric_cols}\nCategorical columns:{categorical_cols}')
	else:
		print('OK.')

	# univariante analysis
	Univariant_analysis(my_data)


	# univariante plots
	Univariant_Plots(my_data)

	# bivariante analysis

	Bivariant_analysis(my_data)
















	# test code
	# df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
    #                      "bar", "bar", "bar", "bar"],
    #                "B": ["one", "one", "one", "two", "two",
    #                      "one", "one", "two", "two"],
    #                "C": ["small", "large", "large", "small",
    #                      "small", "large", "small", "small",
    #                      "large"],
    #                "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
    #                "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
	# print(df)

	# table = pd.pivot_table(df, values='D', index=['A', 'B'],
    #                    columns=['C'], aggfunc="sum")
	# print(table)





