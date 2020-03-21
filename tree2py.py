Air_Pressure = float(input("Enter Air_Pressure : "))
Hour = float(input("Enter Hour : "))
Location = str(input("Enter Location : "))
Month = str(input("Enter Month : "))
Relative_Humidity = float(input("Enter Relative_Humidity : "))
Temperature = float(input("Enter Temperature : "))
def treeFunc(Air_Pressure,Hour,Location,Month,Relative_Humidity,Temperature):
	if Air_Pressure <=  662.5:
		if Relative_Humidity <=  15.23:
			return "VeryGood"
		if Relative_Humidity >  15.23:
			if Hour <=  17:
				if Temperature <=  6.92:
					if Month == "January":
						return "Moderate"
					if Month == "February":
						return "Moderate"
					if Month == "March":
						return "Moderate"
					if Month == "April":
						if Hour <=  9:
							return "UnhealthyForSensitive"
						if Hour >  9:
							return "Moderate"
					if Month == "May":
						return "Moderate"
					if Month == "June":
						return "Moderate"
					if Month == "July":
						return "Moderate"
					if Month == "August":
						return "Moderate"
					if Month == "September":
						return "Moderate"
					if Month == "October":
						return "Moderate"
					if Month == "November":
						return "Moderate"
					if Month == "December":
						return "VeryGood"
				if Temperature >  6.92:
					if Relative_Humidity <=  58.74:
						return "VeryGood"
					if Relative_Humidity >  58.74:
						if Month == "January":
							return "VeryGood"
						if Month == "February":
							return "VeryGood"
						if Month == "March":
							return "VeryGood"
						if Month == "April":
							return "VeryGood"
						if Month == "May":
							return "VeryGood"
						if Month == "June":
							return "VeryGood"
						if Month == "July":
							if Hour <=  4:
								return "VeryGood"
							if Hour >  4:
								if Hour <=  8:
									if Relative_Humidity <=  59:
										return "Moderate"
									if Relative_Humidity >  59:
										if Location == "Pathumthani":
											return "VeryGood"
										if Location == "ChiangRai":
											if Hour <=  6:
												return "VeryGood"
											if Hour >  6:
												return "Moderate"
										if Location == "Tak":
											return "Moderate"
								if Hour >  8:
									return "VeryGood"
						if Month == "August":
							if Hour <=  14:
								return "VeryGood"
							if Hour >  14:
								if Relative_Humidity <=  64.03:
									if Temperature <=  34.31:
										if Air_Pressure <=  252.7:
											return "Moderate"
										if Air_Pressure >  252.7:
											if Air_Pressure <=  252.8:
												return "VeryGood"
											if Air_Pressure >  252.8:
												return "Moderate"
									if Temperature >  34.31:
										return "VeryGood"
								if Relative_Humidity >  64.03:
									return "VeryGood"
						if Month == "September":
							return "UnhealthyForSensitive"
						if Month == "October":
							return "VeryGood"
						if Month == "November":
							return "VeryGood"
						if Month == "December":
							return "VeryGood"
			if Hour >  17:
				if Month == "January":
					return "VeryGood"
				if Month == "February":
					return "Unhealthy"
				if Month == "March":
					return "VeryGood"
				if Month == "April":
					return "VeryGood"
				if Month == "May":
					return "VeryGood"
				if Month == "June":
					return "VeryGood"
				if Month == "July":
					if Location == "Pathumthani":
						return "VeryGood"
					if Location == "ChiangRai":
						return "VeryGood"
					if Location == "Tak":
						if Hour <=  18:
							return "VeryGood"
						if Hour >  18:
							return "Moderate"
				if Month == "August":
					if Temperature <=  29.11:
						return "VeryGood"
					if Temperature >  29.11:
						if Relative_Humidity <=  65.68:
							return "Moderate"
						if Relative_Humidity >  65.68:
							if Relative_Humidity <=  76.24:
								if Air_Pressure <=  253.23:
									return "VeryGood"
								if Air_Pressure >  253.23:
									return "Moderate"
							if Relative_Humidity >  76.24:
								return "VeryGood"
				if Month == "September":
					if Temperature <=  8.21:
						return "VeryGood"
					if Temperature >  8.21:
						if Air_Pressure <=  251.36:
							return "Moderate"
						if Air_Pressure >  251.36:
							return "VeryGood"
				if Month == "October":
					return "VeryGood"
				if Month == "November":
					if Air_Pressure <=  252.44:
						if Relative_Humidity <=  17.52:
							return "VeryGood"
						if Relative_Humidity >  17.52:
							return "Moderate"
					if Air_Pressure >  252.44:
						return "VeryGood"
				if Month == "December":
					return "Moderate"
	if Air_Pressure >  662.5:
		if Month == "January":
			if Hour <=  9:
				if Temperature <=  29.54:
					if Air_Pressure <=  1007.42:
						if Relative_Humidity <=  69.35:
							return "UnhealthyForSensitive"
						if Relative_Humidity >  69.35:
							return "Moderate"
					if Air_Pressure >  1007.42:
						if Relative_Humidity <=  57.72:
							if Air_Pressure <=  1016:
								if Relative_Humidity <=  54.59:
									return "UnhealthyForSensitive"
								if Relative_Humidity >  54.59:
									return "Unhealthy"
							if Air_Pressure >  1016:
								if Temperature <=  27.37:
									return "Moderate"
								if Temperature >  27.37:
									if Relative_Humidity <=  55.25:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  55.25:
										return "Unhealthy"
						if Relative_Humidity >  57.72:
							if Relative_Humidity <=  68.07:
								if Hour <=  5:
									return "UnhealthyForSensitive"
								if Hour >  5:
									if Relative_Humidity <=  60.49:
										if Air_Pressure <=  1013.27:
											if Air_Pressure <=  1011.84:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1011.84:
												return "Unhealthy"
										if Air_Pressure >  1013.27:
											if Relative_Humidity <=  58.98:
												if Air_Pressure <=  1013.95:
													return "Moderate"
												if Air_Pressure >  1013.95:
													return "UnhealthyForSensitive"
											if Relative_Humidity >  58.98:
												return "Moderate"
									if Relative_Humidity >  60.49:
										return "UnhealthyForSensitive"
							if Relative_Humidity >  68.07:
								if Temperature <=  28.43:
									if Air_Pressure <=  1009.69:
										if Hour <=  6:
											return "UnhealthyForSensitive"
										if Hour >  6:
											if Air_Pressure <=  1008.87:
												return "Moderate"
											if Air_Pressure >  1008.87:
												return "UnhealthyForSensitive"
									if Air_Pressure >  1009.69:
										return "Moderate"
								if Temperature >  28.43:
									if Hour <=  2:
										return "Moderate"
									if Hour >  2:
										if Relative_Humidity <=  75.8:
											if Hour <=  6:
												return "Unhealthy"
											if Hour >  6:
												if Relative_Humidity <=  70.64:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  70.64:
													return "Unhealthy"
										if Relative_Humidity >  75.8:
											return "Moderate"
				if Temperature >  29.54:
					if Relative_Humidity <=  64:
						if Air_Pressure <=  1013.75:
							if Relative_Humidity <=  58.69:
								if Air_Pressure <=  1011.64:
									return "Unhealthy"
								if Air_Pressure >  1011.64:
									if Relative_Humidity <=  56.96:
										if Temperature <=  30.47:
											return "UnhealthyForSensitive"
										if Temperature >  30.47:
											return "Unhealthy"
									if Relative_Humidity >  56.96:
										return "Unhealthy"
							if Relative_Humidity >  58.69:
								if Temperature <=  30.9:
									return "UnhealthyForSensitive"
								if Temperature >  30.9:
									if Air_Pressure <=  1010.77:
										return "Unhealthy"
									if Air_Pressure >  1010.77:
										return "UnhealthyForSensitive"
						if Air_Pressure >  1013.75:
							if Temperature <=  29.73:
								return "Unhealthy"
							if Temperature >  29.73:
								if Air_Pressure <=  1016.27:
									if Air_Pressure <=  1014.13:
										return "Moderate"
									if Air_Pressure >  1014.13:
										return "UnhealthyForSensitive"
								if Air_Pressure >  1016.27:
									return "Moderate"
					if Relative_Humidity >  64:
						if Temperature <=  29.77:
							return "UnhealthyForSensitive"
						if Temperature >  29.77:
							return "Unhealthy"
			if Hour >  9:
				if Hour <=  20:
					if Relative_Humidity <=  65.64:
						if Hour <=  12:
							if Temperature <=  27.81:
								if Relative_Humidity <=  55.81:
									return "Moderate"
								if Relative_Humidity >  55.81:
									if Temperature <=  26.56:
										return "Moderate"
									if Temperature >  26.56:
										if Temperature <=  27.55:
											return "UnhealthyForSensitive"
										if Temperature >  27.55:
											if Air_Pressure <=  1011.46:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1011.46:
												return "Moderate"
							if Temperature >  27.81:
								if Relative_Humidity <=  56.63:
									if Temperature <=  28.12:
										return "Moderate"
									if Temperature >  28.12:
										if Hour <=  11:
											if Air_Pressure <=  1013.89:
												return "Unhealthy"
											if Air_Pressure >  1013.89:
												return "UnhealthyForSensitive"
										if Hour >  11:
											return "UnhealthyForSensitive"
								if Relative_Humidity >  56.63:
									if Air_Pressure <=  1012.05:
										if Hour <=  11:
											return "Unhealthy"
										if Hour >  11:
											return "Moderate"
									if Air_Pressure >  1012.05:
										return "Moderate"
						if Hour >  12:
							if Hour <=  18:
								if Air_Pressure <=  1010.57:
									if Relative_Humidity <=  51.9:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  51.9:
										if Air_Pressure <=  1009.36:
											if Temperature <=  27.5:
												if Relative_Humidity <=  64.46:
													return "Moderate"
												if Relative_Humidity >  64.46:
													return "UnhealthyForSensitive"
											if Temperature >  27.5:
												return "UnhealthyForSensitive"
										if Air_Pressure >  1009.36:
											return "Moderate"
								if Air_Pressure >  1010.57:
									return "Moderate"
							if Hour >  18:
								if Relative_Humidity <=  60.09:
									if Temperature <=  29.02:
										if Temperature <=  27.1:
											if Hour <=  19:
												return "Moderate"
											if Hour >  19:
												if Air_Pressure <=  1012.78:
													return "Moderate"
												if Air_Pressure >  1012.78:
													return "UnhealthyForSensitive"
										if Temperature >  27.1:
											return "UnhealthyForSensitive"
									if Temperature >  29.02:
										if Relative_Humidity <=  50.87:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  50.87:
											return "Moderate"
								if Relative_Humidity >  60.09:
									return "Moderate"
					if Relative_Humidity >  65.64:
						if Temperature <=  30.74:
							if Air_Pressure <=  1009.04:
								if Hour <=  14:
									if Temperature <=  27.57:
										return "Moderate"
									if Temperature >  27.57:
										return "UnhealthyForSensitive"
								if Hour >  14:
									if Temperature <=  29.25:
										return "UnhealthyForSensitive"
									if Temperature >  29.25:
										return "Moderate"
							if Air_Pressure >  1009.04:
								if Relative_Humidity <=  66.78:
									return "Moderate"
								if Relative_Humidity >  66.78:
									return "Unhealthy"
						if Temperature >  30.74:
							if Hour <=  15:
								if Relative_Humidity <=  67.41:
									return "UnhealthyForSensitive"
								if Relative_Humidity >  67.41:
									if Hour <=  13:
										return "UnhealthyForSensitive"
									if Hour >  13:
										return "Unhealthy"
							if Hour >  15:
								return "Unhealthy"
				if Hour >  20:
					if Relative_Humidity <=  53.83:
						if Air_Pressure <=  1012.5:
							return "Unhealthy"
						if Air_Pressure >  1012.5:
							if Relative_Humidity <=  52.82:
								return "UnhealthyForSensitive"
							if Relative_Humidity >  52.82:
								return "Unhealthy"
					if Relative_Humidity >  53.83:
						if Relative_Humidity <=  62.65:
							return "UnhealthyForSensitive"
						if Relative_Humidity >  62.65:
							if Temperature <=  30.04:
								if Temperature <=  27.56:
									return "UnhealthyForSensitive"
								if Temperature >  27.56:
									if Temperature <=  29.35:
										return "Moderate"
									if Temperature >  29.35:
										return "UnhealthyForSensitive"
							if Temperature >  30.04:
								return "Unhealthy"
		if Month == "February":
			if Relative_Humidity <=  57.03:
				if Hour <=  8:
					if Air_Pressure <=  1003.06:
						return "UnhealthyForSensitive"
					if Air_Pressure >  1003.06:
						return "Unhealthy"
				if Hour >  8:
					if Relative_Humidity <=  51.47:
						if Hour <=  19:
							if Hour <=  10:
								return "Unhealthy"
							if Hour >  10:
								if Air_Pressure <=  1009.68:
									return "Unhealthy"
								if Air_Pressure >  1009.68:
									if Air_Pressure <=  1013.93:
										if Air_Pressure <=  1010.66:
											if Hour <=  18:
												if Relative_Humidity <=  46.45:
													if Relative_Humidity <=  44.43:
														return "UnhealthyForSensitive"
													if Relative_Humidity >  44.43:
														return "Moderate"
												if Relative_Humidity >  46.45:
													return "UnhealthyForSensitive"
											if Hour >  18:
												return "Unhealthy"
										if Air_Pressure >  1010.66:
											if Relative_Humidity <=  42.63:
												return "Unhealthy"
											if Relative_Humidity >  42.63:
												return "UnhealthyForSensitive"
									if Air_Pressure >  1013.93:
										if Relative_Humidity <=  46.65:
											return "Unhealthy"
										if Relative_Humidity >  46.65:
											return "UnhealthyForSensitive"
						if Hour >  19:
							if Air_Pressure <=  1012.97:
								if Temperature <=  29.02:
									return "UnhealthyForSensitive"
								if Temperature >  29.02:
									return "Unhealthy"
							if Air_Pressure >  1012.97:
								return "Unhealthy"
					if Relative_Humidity >  51.47:
						if Temperature <=  29.16:
							if Relative_Humidity <=  53.57:
								if Hour <=  10:
									return "Unhealthy"
								if Hour >  10:
									if Temperature <=  28.92:
										if Relative_Humidity <=  51.8:
											return "Unhealthy"
										if Relative_Humidity >  51.8:
											return "Moderate"
									if Temperature >  28.92:
										if Temperature <=  28.97:
											return "UnhealthyForSensitive"
										if Temperature >  28.97:
											return "Moderate"
							if Relative_Humidity >  53.57:
								return "Moderate"
						if Temperature >  29.16:
							if Hour <=  11:
								if Temperature <=  31.09:
									if Air_Pressure <=  1017.04:
										if Air_Pressure <=  1012.6:
											if Relative_Humidity <=  54.79:
												return "Unhealthy"
											if Relative_Humidity >  54.79:
												return "UnhealthyForSensitive"
										if Air_Pressure >  1012.6:
											return "Unhealthy"
									if Air_Pressure >  1017.04:
										return "UnhealthyForSensitive"
								if Temperature >  31.09:
									return "UnhealthyForSensitive"
							if Hour >  11:
								if Air_Pressure <=  997.3:
									return "Unhealthy"
								if Air_Pressure >  997.3:
									if Hour <=  17:
										return "UnhealthyForSensitive"
									if Hour >  17:
										if Relative_Humidity <=  54.33:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  54.33:
											if Relative_Humidity <=  55.39:
												return "Moderate"
											if Relative_Humidity >  55.39:
												if Hour <=  20:
													if Hour <=  19:
														return "UnhealthyForSensitive"
													if Hour >  19:
														return "Moderate"
												if Hour >  20:
													return "UnhealthyForSensitive"
			if Relative_Humidity >  57.03:
				if Relative_Humidity <=  63.01:
					if Air_Pressure <=  1008.66:
						return "UnhealthyForSensitive"
					if Air_Pressure >  1008.66:
						if Temperature <=  30.64:
							if Relative_Humidity <=  57.42:
								return "Unhealthy"
							if Relative_Humidity >  57.42:
								if Temperature <=  30.41:
									return "Moderate"
								if Temperature >  30.41:
									if Relative_Humidity <=  61.07:
										return "Moderate"
									if Relative_Humidity >  61.07:
										return "Unhealthy"
						if Temperature >  30.64:
							if Hour <=  15:
								if Temperature <=  31.44:
									if Hour <=  3:
										return "UnhealthyForSensitive"
									if Hour >  3:
										if Hour <=  12:
											return "Unhealthy"
										if Hour >  12:
											return "UnhealthyForSensitive"
								if Temperature >  31.44:
									if Relative_Humidity <=  59.07:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  59.07:
										if Temperature <=  32.77:
											if Hour <=  10:
												if Relative_Humidity <=  61.22:
													if Temperature <=  32.65:
														return "Moderate"
													if Temperature >  32.65:
														return "UnhealthyForSensitive"
												if Relative_Humidity >  61.22:
													return "UnhealthyForSensitive"
											if Hour >  10:
												return "Unhealthy"
										if Temperature >  32.77:
											if Hour <=  7:
												if Temperature <=  33.13:
													if Air_Pressure <=  1011.11:
														if Air_Pressure <=  1009.94:
															return "Unhealthy"
														if Air_Pressure >  1009.94:
															return "Moderate"
													if Air_Pressure >  1011.11:
														return "Unhealthy"
												if Temperature >  33.13:
													return "Unhealthy"
											if Hour >  7:
												return "UnhealthyForSensitive"
							if Hour >  15:
								if Temperature <=  33.21:
									if Air_Pressure <=  1011.66:
										return "Moderate"
									if Air_Pressure >  1011.66:
										return "UnhealthyForSensitive"
								if Temperature >  33.21:
									return "Unhealthy"
				if Relative_Humidity >  63.01:
					if Temperature <=  32.49:
						return "UnhealthyForSensitive"
					if Temperature >  32.49:
						if Relative_Humidity <=  64.36:
							return "Moderate"
						if Relative_Humidity >  64.36:
							return "UnhealthyForSensitive"
		if Month == "March":
			if Air_Pressure <=  998.5:
				if Temperature <=  30.92:
					if Air_Pressure <=  971.8:
						return "Moderate"
					if Air_Pressure >  971.8:
						if Location == "Pathumthani":
							return "Unhealthy"
						if Location == "ChiangRai":
							if Air_Pressure <=  996.64:
								return "VeryUnhealthy"
							if Air_Pressure >  996.64:
								return "Unhealthy"
						if Location == "Tak":
							if Hour <=  4:
								return "Unhealthy"
							if Hour >  4:
								return "VeryUnhealthy"
				if Temperature >  30.92:
					if Relative_Humidity <=  50.59:
						if Hour <=  13:
							return "Unhealthy"
						if Hour >  13:
							if Air_Pressure <=  995.62:
								return "Unhealthy"
							if Air_Pressure >  995.62:
								if Temperature <=  34.76:
									return "Unhealthy"
								if Temperature >  34.76:
									return "UnhealthyForSensitive"
					if Relative_Humidity >  50.59:
						if Hour <=  3:
							if Relative_Humidity <=  64.05:
								return "Unhealthy"
							if Relative_Humidity >  64.05:
								return "UnhealthyForSensitive"
						if Hour >  3:
							if Hour <=  19:
								if Hour <=  9:
									if Hour <=  8:
										if Temperature <=  31.92:
											return "Unhealthy"
										if Temperature >  31.92:
											return "Moderate"
									if Hour >  8:
										if Temperature <=  32.85:
											return "VeryUnhealthy"
										if Temperature >  32.85:
											return "Unhealthy"
								if Hour >  9:
									if Temperature <=  33.37:
										return "UnhealthyForSensitive"
									if Temperature >  33.37:
										if Hour <=  12:
											return "Unhealthy"
										if Hour >  12:
											if Hour <=  18:
												if Air_Pressure <=  994.44:
													return "UnhealthyForSensitive"
												if Air_Pressure >  994.44:
													if Air_Pressure <=  997.83:
														return "Moderate"
													if Air_Pressure >  997.83:
														return "UnhealthyForSensitive"
											if Hour >  18:
												if Relative_Humidity <=  52.45:
													return "Unhealthy"
												if Relative_Humidity >  52.45:
													return "UnhealthyForSensitive"
							if Hour >  19:
								if Air_Pressure <=  992.74:
									if Temperature <=  32.91:
										if Relative_Humidity <=  58.53:
											return "Unhealthy"
										if Relative_Humidity >  58.53:
											return "UnhealthyForSensitive"
									if Temperature >  32.91:
										if Relative_Humidity <=  53.73:
											return "Moderate"
										if Relative_Humidity >  53.73:
											return "UnhealthyForSensitive"
								if Air_Pressure >  992.74:
									return "Unhealthy"
			if Air_Pressure >  998.5:
				if Relative_Humidity <=  57.14:
					if Temperature <=  34.29:
						if Relative_Humidity <=  51.89:
							return "Unhealthy"
						if Relative_Humidity >  51.89:
							if Hour <=  11:
								if Temperature <=  32.69:
									if Hour <=  8:
										if Hour <=  0:
											if Relative_Humidity <=  54.43:
												return "Unhealthy"
											if Relative_Humidity >  54.43:
												return "UnhealthyForSensitive"
										if Hour >  0:
											if Air_Pressure <=  1002.67:
												if Relative_Humidity <=  56:
													return "Unhealthy"
												if Relative_Humidity >  56:
													if Temperature <=  31.59:
														return "VeryUnhealthy"
													if Temperature >  31.59:
														return "UnhealthyForSensitive"
											if Air_Pressure >  1002.67:
												return "Unhealthy"
									if Hour >  8:
										if Air_Pressure <=  1011.2:
											if Air_Pressure <=  1008.04:
												if Temperature <=  31.56:
													return "UnhealthyForSensitive"
												if Temperature >  31.56:
													return "VeryUnhealthy"
											if Air_Pressure >  1008.04:
												return "UnhealthyForSensitive"
										if Air_Pressure >  1011.2:
											if Air_Pressure <=  1011.75:
												return "Moderate"
											if Air_Pressure >  1011.75:
												return "Unhealthy"
								if Temperature >  32.69:
									if Relative_Humidity <=  56.15:
										if Relative_Humidity <=  55.73:
											if Relative_Humidity <=  54.49:
												if Air_Pressure <=  1000.79:
													return "UnhealthyForSensitive"
												if Air_Pressure >  1000.79:
													return "Unhealthy"
											if Relative_Humidity >  54.49:
												if Hour <=  2:
													return "Moderate"
												if Hour >  2:
													return "UnhealthyForSensitive"
										if Relative_Humidity >  55.73:
											return "Unhealthy"
									if Relative_Humidity >  56.15:
										if Hour <=  6:
											if Hour <=  1:
												return "Moderate"
											if Hour >  1:
												return "Unhealthy"
										if Hour >  6:
											return "Moderate"
							if Hour >  11:
								if Air_Pressure <=  1004.25:
									if Relative_Humidity <=  53.8:
										if Hour <=  21:
											return "Moderate"
										if Hour >  21:
											return "Unhealthy"
									if Relative_Humidity >  53.8:
										return "Moderate"
								if Air_Pressure >  1004.25:
									if Air_Pressure <=  1007.13:
										if Temperature <=  30.33:
											if Hour <=  18:
												return "Unhealthy"
											if Hour >  18:
												return "UnhealthyForSensitive"
										if Temperature >  30.33:
											return "UnhealthyForSensitive"
									if Air_Pressure >  1007.13:
										if Air_Pressure <=  1011.08:
											if Air_Pressure <=  1010.73:
												if Temperature <=  27.81:
													return "Unhealthy"
												if Temperature >  27.81:
													return "UnhealthyForSensitive"
											if Air_Pressure >  1010.73:
												return "Unhealthy"
										if Air_Pressure >  1011.08:
											return "Moderate"
					if Temperature >  34.29:
						if Relative_Humidity <=  55.17:
							if Hour <=  14:
								if Air_Pressure <=  1008.8:
									if Relative_Humidity <=  40.71:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  40.71:
										if Air_Pressure <=  1000.91:
											return "Unhealthy"
										if Air_Pressure >  1000.91:
											if Air_Pressure <=  1003.12:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1003.12:
												if Temperature <=  35.57:
													return "Unhealthy"
												if Temperature >  35.57:
													return "UnhealthyForSensitive"
								if Air_Pressure >  1008.8:
									return "UnhealthyForSensitive"
							if Hour >  14:
								return "UnhealthyForSensitive"
						if Relative_Humidity >  55.17:
							return "Moderate"
				if Relative_Humidity >  57.14:
					if Location == "Pathumthani":
						if Relative_Humidity <=  59.66:
							if Temperature <=  30.89:
								if Temperature <=  29.68:
									if Temperature <=  28.17:
										if Relative_Humidity <=  58.54:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  58.54:
											return "Unhealthy"
									if Temperature >  28.17:
										return "Unhealthy"
								if Temperature >  29.68:
									if Temperature <=  30.66:
										return "UnhealthyForSensitive"
									if Temperature >  30.66:
										return "Unhealthy"
							if Temperature >  30.89:
								if Hour <=  3:
									if Temperature <=  32.56:
										return "UnhealthyForSensitive"
									if Temperature >  32.56:
										if Hour <=  1:
											return "Moderate"
										if Hour >  1:
											if Air_Pressure <=  1007.31:
												return "Moderate"
											if Air_Pressure >  1007.31:
												if Relative_Humidity <=  58.93:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  58.93:
													if Relative_Humidity <=  59.36:
														return "Moderate"
													if Relative_Humidity >  59.36:
														return "UnhealthyForSensitive"
								if Hour >  3:
									if Hour <=  19:
										if Temperature <=  31.52:
											if Hour <=  10:
												return "UnhealthyForSensitive"
											if Hour >  10:
												return "Moderate"
										if Temperature >  31.52:
											if Air_Pressure <=  1004.05:
												if Hour <=  8:
													return "UnhealthyForSensitive"
												if Hour >  8:
													return "Moderate"
											if Air_Pressure >  1004.05:
												return "Unhealthy"
									if Hour >  19:
										return "UnhealthyForSensitive"
						if Relative_Humidity >  59.66:
							if Hour <=  5:
								if Air_Pressure <=  1008.94:
									return "UnhealthyForSensitive"
								if Air_Pressure >  1008.94:
									if Relative_Humidity <=  65.94:
										if Temperature <=  29.94:
											return "Unhealthy"
										if Temperature >  29.94:
											if Hour <=  4:
												if Temperature <=  32.57:
													if Temperature <=  31.6:
														if Relative_Humidity <=  63.76:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  63.76:
															return "Moderate"
													if Temperature >  31.6:
														return "Moderate"
												if Temperature >  32.57:
													return "UnhealthyForSensitive"
											if Hour >  4:
												return "UnhealthyForSensitive"
									if Relative_Humidity >  65.94:
										return "Moderate"
							if Hour >  5:
								if Temperature <=  32.14:
									if Air_Pressure <=  1006.63:
										return "UnhealthyForSensitive"
									if Air_Pressure >  1006.63:
										if Relative_Humidity <=  64.98:
											if Temperature <=  27.73:
												if Hour <=  16:
													if Hour <=  13:
														return "UnhealthyForSensitive"
													if Hour >  13:
														return "Moderate"
												if Hour >  16:
													return "UnhealthyForSensitive"
											if Temperature >  27.73:
												if Air_Pressure <=  1012.62:
													if Air_Pressure <=  1011.28:
														if Temperature <=  31.75:
															return "Moderate"
														if Temperature >  31.75:
															if Hour <=  8:
																if Relative_Humidity <=  62.52:
																	return "UnhealthyForSensitive"
																if Relative_Humidity >  62.52:
																	return "Moderate"
															if Hour >  8:
																return "Unhealthy"
													if Air_Pressure >  1011.28:
														if Air_Pressure <=  1011.55:
															return "Unhealthy"
														if Air_Pressure >  1011.55:
															return "Moderate"
												if Air_Pressure >  1012.62:
													return "UnhealthyForSensitive"
										if Relative_Humidity >  64.98:
											if Air_Pressure <=  1009:
												if Temperature <=  27.88:
													return "UnhealthyForSensitive"
												if Temperature >  27.88:
													if Hour <=  16:
														if Air_Pressure <=  1008.74:
															if Relative_Humidity <=  67.48:
																return "UnhealthyForSensitive"
															if Relative_Humidity >  67.48:
																if Hour <=  6:
																	return "UnhealthyForSensitive"
																if Hour >  6:
																	if Hour <=  13:
																		return "Unhealthy"
																	if Hour >  13:
																		return "UnhealthyForSensitive"
														if Air_Pressure >  1008.74:
															return "Unhealthy"
													if Hour >  16:
														if Hour <=  18:
															return "Moderate"
														if Hour >  18:
															return "UnhealthyForSensitive"
											if Air_Pressure >  1009:
												if Hour <=  13:
													if Temperature <=  30.64:
														if Relative_Humidity <=  69.59:
															if Hour <=  9:
																return "Unhealthy"
															if Hour >  9:
																if Relative_Humidity <=  65.92:
																	return "Moderate"
																if Relative_Humidity >  65.92:
																	return "UnhealthyForSensitive"
														if Relative_Humidity >  69.59:
															if Air_Pressure <=  1014.21:
																if Temperature <=  29.53:
																	if Relative_Humidity <=  73.69:
																		return "UnhealthyForSensitive"
																	if Relative_Humidity >  73.69:
																		return "Moderate"
																if Temperature >  29.53:
																	return "UnhealthyForSensitive"
															if Air_Pressure >  1014.21:
																return "Moderate"
													if Temperature >  30.64:
														if Air_Pressure <=  1010.43:
															if Temperature <=  31.73:
																return "UnhealthyForSensitive"
															if Temperature >  31.73:
																return "Moderate"
														if Air_Pressure >  1010.43:
															if Relative_Humidity <=  76:
																return "Moderate"
															if Relative_Humidity >  76:
																return "UnhealthyForSensitive"
												if Hour >  13:
													if Hour <=  18:
														return "Moderate"
													if Hour >  18:
														if Air_Pressure <=  1011.95:
															return "UnhealthyForSensitive"
														if Air_Pressure >  1011.95:
															if Air_Pressure <=  1014.11:
																return "Moderate"
															if Air_Pressure >  1014.11:
																return "UnhealthyForSensitive"
								if Temperature >  32.14:
									if Air_Pressure <=  1010.45:
										if Temperature <=  32.7:
											if Hour <=  7:
												if Relative_Humidity <=  62.79:
													return "Unhealthy"
												if Relative_Humidity >  62.79:
													return "UnhealthyForSensitive"
											if Hour >  7:
												if Hour <=  22:
													return "Unhealthy"
												if Hour >  22:
													return "UnhealthyForSensitive"
										if Temperature >  32.7:
											if Hour <=  10:
												if Relative_Humidity <=  61.86:
													return "Moderate"
												if Relative_Humidity >  61.86:
													return "UnhealthyForSensitive"
											if Hour >  10:
												if Hour <=  12:
													if Relative_Humidity <=  62.23:
														return "Unhealthy"
													if Relative_Humidity >  62.23:
														return "UnhealthyForSensitive"
												if Hour >  12:
													if Relative_Humidity <=  67.64:
														return "UnhealthyForSensitive"
													if Relative_Humidity >  67.64:
														return "Moderate"
									if Air_Pressure >  1010.45:
										if Relative_Humidity <=  62.45:
											return "Moderate"
										if Relative_Humidity >  62.45:
											return "UnhealthyForSensitive"
					if Location == "ChiangRai":
						return "Moderate"
					if Location == "Tak":
						return "Moderate"
		if Month == "April":
			if Air_Pressure <=  999.28:
				if Hour <=  10:
					if Temperature <=  28.49:
						if Relative_Humidity <=  55.73:
							return "VeryGood"
						if Relative_Humidity >  55.73:
							return "Unhealthy"
					if Temperature >  28.49:
						if Air_Pressure <=  997.98:
							if Relative_Humidity <=  55.4:
								if Temperature <=  30.33:
									if Relative_Humidity <=  52.71:
										return "Hazardous"
									if Relative_Humidity >  52.71:
										return "VeryUnhealthy"
								if Temperature >  30.33:
									if Hour <=  8:
										if Relative_Humidity <=  46.75:
											if Hour <=  2:
												return "VeryUnhealthy"
											if Hour >  2:
												return "Hazardous"
										if Relative_Humidity >  46.75:
											if Hour <=  2:
												if Air_Pressure <=  993.53:
													if Relative_Humidity <=  50.48:
														return "Unhealthy"
													if Relative_Humidity >  50.48:
														return "UnhealthyForSensitive"
												if Air_Pressure >  993.53:
													if Temperature <=  31.82:
														return "Unhealthy"
													if Temperature >  31.82:
														if Relative_Humidity <=  53.36:
															return "Unhealthy"
														if Relative_Humidity >  53.36:
															return "UnhealthyForSensitive"
											if Hour >  2:
												if Hour <=  6:
													if Temperature <=  31.66:
														return "UnhealthyForSensitive"
													if Temperature >  31.66:
														if Air_Pressure <=  995.97:
															return "VeryUnhealthy"
														if Air_Pressure >  995.97:
															return "Hazardous"
												if Hour >  6:
													if Hour <=  7:
														return "VeryUnhealthy"
													if Hour >  7:
														if Air_Pressure <=  990.27:
															return "UnhealthyForSensitive"
														if Air_Pressure >  990.27:
															return "Unhealthy"
									if Hour >  8:
										if Temperature <=  34.05:
											return "Unhealthy"
										if Temperature >  34.05:
											if Relative_Humidity <=  42.44:
												return "VeryUnhealthy"
											if Relative_Humidity >  42.44:
												if Hour <=  9:
													if Air_Pressure <=  997.37:
														return "UnhealthyForSensitive"
													if Air_Pressure >  997.37:
														return "Unhealthy"
												if Hour >  9:
													if Temperature <=  35.24:
														return "UnhealthyForSensitive"
													if Temperature >  35.24:
														if Temperature <=  36.4:
															return "Unhealthy"
														if Temperature >  36.4:
															return "UnhealthyForSensitive"
							if Relative_Humidity >  55.4:
								if Hour <=  4:
									if Temperature <=  31.98:
										if Air_Pressure <=  995.56:
											if Temperature <=  29.97:
												if Temperature <=  29.16:
													return "Unhealthy"
												if Temperature >  29.16:
													return "UnhealthyForSensitive"
											if Temperature >  29.97:
												return "Unhealthy"
										if Air_Pressure >  995.56:
											if Hour <=  2:
												if Relative_Humidity <=  64.08:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  64.08:
													return "Unhealthy"
											if Hour >  2:
												if Relative_Humidity <=  59.44:
													if Relative_Humidity <=  57.34:
														return "Unhealthy"
													if Relative_Humidity >  57.34:
														return "VeryUnhealthy"
												if Relative_Humidity >  59.44:
													return "UnhealthyForSensitive"
									if Temperature >  31.98:
										return "UnhealthyForSensitive"
								if Hour >  4:
									return "Unhealthy"
						if Air_Pressure >  997.98:
							if Relative_Humidity <=  62.15:
								if Hour <=  7:
									if Air_Pressure <=  998.89:
										return "Unhealthy"
									if Air_Pressure >  998.89:
										return "UnhealthyForSensitive"
								if Hour >  7:
									return "Unhealthy"
							if Relative_Humidity >  62.15:
								return "Moderate"
				if Hour >  10:
					if Hour <=  21:
						if Air_Pressure <=  996.36:
							if Relative_Humidity <=  51.66:
								if Hour <=  17:
									if Hour <=  13:
										if Temperature <=  34.78:
											if Relative_Humidity <=  45.64:
												return "VeryGood"
											if Relative_Humidity >  45.64:
												return "Unhealthy"
										if Temperature >  34.78:
											if Relative_Humidity <=  35.92:
												return "Unhealthy"
											if Relative_Humidity >  35.92:
												return "UnhealthyForSensitive"
									if Hour >  13:
										if Relative_Humidity <=  43.97:
											if Air_Pressure <=  994.29:
												return "UnhealthyForSensitive"
											if Air_Pressure >  994.29:
												if Hour <=  14:
													return "UnhealthyForSensitive"
												if Hour >  14:
													return "Moderate"
										if Relative_Humidity >  43.97:
											if Temperature <=  32.74:
												return "Moderate"
											if Temperature >  32.74:
												if Hour <=  15:
													if Temperature <=  34.38:
														return "Moderate"
													if Temperature >  34.38:
														return "Unhealthy"
												if Hour >  15:
													return "Unhealthy"
								if Hour >  17:
									if Temperature <=  34.97:
										if Relative_Humidity <=  43.88:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  43.88:
											if Temperature <=  34.37:
												return "UnhealthyForSensitive"
											if Temperature >  34.37:
												return "Unhealthy"
									if Temperature >  34.97:
										return "Unhealthy"
							if Relative_Humidity >  51.66:
								if Relative_Humidity <=  53.85:
									if Relative_Humidity <=  52.39:
										return "VeryGood"
									if Relative_Humidity >  52.39:
										if Relative_Humidity <=  53.78:
											return "Moderate"
										if Relative_Humidity >  53.78:
											return "Unhealthy"
								if Relative_Humidity >  53.85:
									if Hour <=  19:
										if Relative_Humidity <=  55.59:
											return "Unhealthy"
										if Relative_Humidity >  55.59:
											return "Moderate"
									if Hour >  19:
										if Temperature <=  31.39:
											return "UnhealthyForSensitive"
										if Temperature >  31.39:
											return "Unhealthy"
						if Air_Pressure >  996.36:
							if Hour <=  12:
								if Air_Pressure <=  997.44:
									return "UnhealthyForSensitive"
								if Air_Pressure >  997.44:
									return "Unhealthy"
							if Hour >  12:
								if Hour <=  19:
									return "Moderate"
								if Hour >  19:
									if Hour <=  20:
										if Air_Pressure <=  997.02:
											return "Unhealthy"
										if Air_Pressure >  997.02:
											return "Moderate"
									if Hour >  20:
										return "UnhealthyForSensitive"
					if Hour >  21:
						if Temperature <=  31.82:
							if Air_Pressure <=  987.42:
								if Relative_Humidity <=  57.11:
									return "Moderate"
								if Relative_Humidity >  57.11:
									return "Unhealthy"
							if Air_Pressure >  987.42:
								if Relative_Humidity <=  56.63:
									return "Unhealthy"
								if Relative_Humidity >  56.63:
									if Temperature <=  30.43:
										return "Unhealthy"
									if Temperature >  30.43:
										return "UnhealthyForSensitive"
						if Temperature >  31.82:
							if Relative_Humidity <=  49.12:
								if Hour <=  22:
									if Air_Pressure <=  983.37:
										return "Unhealthy"
									if Air_Pressure >  983.37:
										if Air_Pressure <=  995.17:
											return "UnhealthyForSensitive"
										if Air_Pressure >  995.17:
											return "Unhealthy"
								if Hour >  22:
									return "Unhealthy"
							if Relative_Humidity >  49.12:
								if Relative_Humidity <=  54.11:
									return "UnhealthyForSensitive"
								if Relative_Humidity >  54.11:
									if Air_Pressure <=  995.28:
										return "UnhealthyForSensitive"
									if Air_Pressure >  995.28:
										return "Unhealthy"
			if Air_Pressure >  999.28:
				if Temperature <=  34.19:
					if Temperature <=  31.09:
						if Air_Pressure <=  1004.83:
							if Relative_Humidity <=  63.69:
								if Temperature <=  28.22:
									if Hour <=  4:
										return "VeryGood"
									if Hour >  4:
										return "Moderate"
								if Temperature >  28.22:
									if Hour <=  18:
										if Relative_Humidity <=  61.23:
											if Relative_Humidity <=  49.74:
												return "VeryGood"
											if Relative_Humidity >  49.74:
												if Hour <=  15:
													return "Unhealthy"
												if Hour >  15:
													if Relative_Humidity <=  56.93:
														return "UnhealthyForSensitive"
													if Relative_Humidity >  56.93:
														return "Unhealthy"
										if Relative_Humidity >  61.23:
											if Temperature <=  29.8:
												if Hour <=  16:
													if Relative_Humidity <=  62.26:
														return "Unhealthy"
													if Relative_Humidity >  62.26:
														return "VeryGood"
												if Hour >  16:
													return "Moderate"
											if Temperature >  29.8:
												return "VeryGood"
									if Hour >  18:
										if Temperature <=  29.78:
											return "VeryGood"
										if Temperature >  29.78:
											return "Moderate"
							if Relative_Humidity >  63.69:
								if Air_Pressure <=  1000.2:
									if Hour <=  3:
										return "Moderate"
									if Hour >  3:
										return "UnhealthyForSensitive"
								if Air_Pressure >  1000.2:
									return "Moderate"
						if Air_Pressure >  1004.83:
							if Relative_Humidity <=  67.09:
								if Relative_Humidity <=  55.23:
									return "UnhealthyForSensitive"
								if Relative_Humidity >  55.23:
									if Air_Pressure <=  1006.86:
										if Temperature <=  29.25:
											if Temperature <=  29.02:
												if Hour <=  13:
													return "Unhealthy"
												if Hour >  13:
													if Air_Pressure <=  1005.53:
														return "Unhealthy"
													if Air_Pressure >  1005.53:
														return "UnhealthyForSensitive"
											if Temperature >  29.02:
												if Air_Pressure <=  1005.66:
													return "Moderate"
												if Air_Pressure >  1005.66:
													return "VeryGood"
										if Temperature >  29.25:
											if Relative_Humidity <=  58.44:
												if Hour <=  15:
													return "Unhealthy"
												if Hour >  15:
													return "Moderate"
											if Relative_Humidity >  58.44:
												return "Moderate"
									if Air_Pressure >  1006.86:
										if Temperature <=  26.32:
											return "Moderate"
										if Temperature >  26.32:
											if Temperature <=  28.35:
												if Relative_Humidity <=  57.39:
													if Relative_Humidity <=  56.99:
														return "UnhealthyForSensitive"
													if Relative_Humidity >  56.99:
														return "Moderate"
												if Relative_Humidity >  57.39:
													return "UnhealthyForSensitive"
											if Temperature >  28.35:
												if Relative_Humidity <=  58.87:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  58.87:
													if Hour <=  4:
														if Air_Pressure <=  1010.65:
															return "Unhealthy"
														if Air_Pressure >  1010.65:
															return "UnhealthyForSensitive"
													if Hour >  4:
														if Relative_Humidity <=  61.51:
															if Air_Pressure <=  1008.92:
																if Hour <=  14:
																	return "Unhealthy"
																if Hour >  14:
																	return "Moderate"
															if Air_Pressure >  1008.92:
																return "UnhealthyForSensitive"
														if Relative_Humidity >  61.51:
															return "Moderate"
							if Relative_Humidity >  67.09:
								if Temperature <=  26.85:
									return "Unhealthy"
								if Temperature >  26.85:
									if Air_Pressure <=  1011.65:
										if Relative_Humidity <=  72.41:
											if Hour <=  4:
												if Air_Pressure <=  1008.21:
													return "Unhealthy"
												if Air_Pressure >  1008.21:
													return "Moderate"
											if Hour >  4:
												if Temperature <=  27.33:
													if Air_Pressure <=  1006.62:
														return "UnhealthyForSensitive"
													if Air_Pressure >  1006.62:
														return "Unhealthy"
												if Temperature >  27.33:
													if Hour <=  9:
														return "UnhealthyForSensitive"
													if Hour >  9:
														return "Moderate"
										if Relative_Humidity >  72.41:
											if Temperature <=  28.71:
												if Relative_Humidity <=  73.42:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  73.42:
													return "Moderate"
											if Temperature >  28.71:
												return "UnhealthyForSensitive"
									if Air_Pressure >  1011.65:
										if Relative_Humidity <=  71.17:
											if Hour <=  7:
												return "Unhealthy"
											if Hour >  7:
												if Air_Pressure <=  1013.87:
													return "Moderate"
												if Air_Pressure >  1013.87:
													return "Unhealthy"
										if Relative_Humidity >  71.17:
											return "VeryGood"
					if Temperature >  31.09:
						if Air_Pressure <=  1008.79:
							if Temperature <=  33.4:
								if Hour <=  7:
									if Relative_Humidity <=  59.77:
										if Air_Pressure <=  1008.09:
											return "UnhealthyForSensitive"
										if Air_Pressure >  1008.09:
											return "VeryGood"
									if Relative_Humidity >  59.77:
										if Air_Pressure <=  1006.75:
											if Temperature <=  32.24:
												if Relative_Humidity <=  62.22:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  62.22:
													return "Moderate"
											if Temperature >  32.24:
												return "VeryGood"
										if Air_Pressure >  1006.75:
											if Temperature <=  32.33:
												return "Moderate"
											if Temperature >  32.33:
												if Air_Pressure <=  1008.29:
													return "Moderate"
												if Air_Pressure >  1008.29:
													if Air_Pressure <=  1008.53:
														return "UnhealthyForSensitive"
													if Air_Pressure >  1008.53:
														return "Moderate"
								if Hour >  7:
									if Relative_Humidity <=  66.66:
										if Temperature <=  31.5:
											if Air_Pressure <=  1000.46:
												return "Moderate"
											if Air_Pressure >  1000.46:
												return "UnhealthyForSensitive"
										if Temperature >  31.5:
											if Relative_Humidity <=  55.6:
												if Temperature <=  32.7:
													if Hour <=  18:
														return "UnhealthyForSensitive"
													if Hour >  18:
														return "VeryGood"
												if Temperature >  32.7:
													return "Unhealthy"
											if Relative_Humidity >  55.6:
												if Hour <=  14:
													if Hour <=  8:
														return "Moderate"
													if Hour >  8:
														if Temperature <=  32.19:
															return "Moderate"
														if Temperature >  32.19:
															return "UnhealthyForSensitive"
												if Hour >  14:
													if Relative_Humidity <=  61.2:
														return "Moderate"
													if Relative_Humidity >  61.2:
														if Temperature <=  32.89:
															return "VeryGood"
														if Temperature >  32.89:
															return "Moderate"
									if Relative_Humidity >  66.66:
										if Relative_Humidity <=  71.49:
											if Air_Pressure <=  1007.99:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1007.99:
												return "VeryGood"
										if Relative_Humidity >  71.49:
											if Hour <=  16:
												return "UnhealthyForSensitive"
											if Hour >  16:
												return "Unhealthy"
							if Temperature >  33.4:
								if Temperature <=  33.84:
									if Hour <=  4:
										if Air_Pressure <=  1007.11:
											return "UnhealthyForSensitive"
										if Air_Pressure >  1007.11:
											return "Moderate"
									if Hour >  4:
										if Air_Pressure <=  1006.19:
											return "Moderate"
										if Air_Pressure >  1006.19:
											if Hour <=  20:
												return "UnhealthyForSensitive"
											if Hour >  20:
												return "Moderate"
								if Temperature >  33.84:
									if Temperature <=  34.11:
										return "Moderate"
									if Temperature >  34.11:
										return "UnhealthyForSensitive"
						if Air_Pressure >  1008.79:
							if Temperature <=  32.75:
								if Temperature <=  32.29:
									if Air_Pressure <=  1012.12:
										if Hour <=  11:
											if Relative_Humidity <=  53.65:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  53.65:
												return "Moderate"
										if Hour >  11:
											if Hour <=  20:
												if Hour <=  17:
													return "VeryGood"
												if Hour >  17:
													return "UnhealthyForSensitive"
											if Hour >  20:
												return "Moderate"
									if Air_Pressure >  1012.12:
										return "UnhealthyForSensitive"
								if Temperature >  32.29:
									if Air_Pressure <=  1010.56:
										if Relative_Humidity <=  70.06:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  70.06:
											return "Moderate"
									if Air_Pressure >  1010.56:
										return "Moderate"
							if Temperature >  32.75:
								if Hour <=  6:
									return "Moderate"
								if Hour >  6:
									if Relative_Humidity <=  68.06:
										if Relative_Humidity <=  60.52:
											if Hour <=  11:
												if Hour <=  9:
													if Temperature <=  33.36:
														return "UnhealthyForSensitive"
													if Temperature >  33.36:
														if Relative_Humidity <=  58.91:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  58.91:
															return "Unhealthy"
												if Hour >  9:
													return "Unhealthy"
											if Hour >  11:
												if Temperature <=  33.66:
													if Temperature <=  33.15:
														return "Moderate"
													if Temperature >  33.15:
														return "UnhealthyForSensitive"
												if Temperature >  33.66:
													return "Moderate"
										if Relative_Humidity >  60.52:
											if Temperature <=  33.16:
												return "Moderate"
											if Temperature >  33.16:
												if Air_Pressure <=  1009.33:
													return "UnhealthyForSensitive"
												if Air_Pressure >  1009.33:
													if Hour <=  11:
														return "Moderate"
													if Hour >  11:
														return "UnhealthyForSensitive"
									if Relative_Humidity >  68.06:
										return "UnhealthyForSensitive"
				if Temperature >  34.19:
					if Hour <=  10:
						if Temperature <=  35.14:
							return "Unhealthy"
						if Temperature >  35.14:
							return "UnhealthyForSensitive"
					if Hour >  10:
						if Air_Pressure <=  1000.47:
							if Relative_Humidity <=  44.55:
								return "VeryGood"
							if Relative_Humidity >  44.55:
								return "UnhealthyForSensitive"
						if Air_Pressure >  1000.47:
							if Temperature <=  36.02:
								if Relative_Humidity <=  61.25:
									return "Moderate"
								if Relative_Humidity >  61.25:
									if Hour <=  13:
										return "Moderate"
									if Hour >  13:
										if Air_Pressure <=  1006.97:
											return "Moderate"
										if Air_Pressure >  1006.97:
											return "UnhealthyForSensitive"
							if Temperature >  36.02:
								if Hour <=  15:
									return "Unhealthy"
								if Hour >  15:
									if Relative_Humidity <=  49.59:
										return "Unhealthy"
									if Relative_Humidity >  49.59:
										return "UnhealthyForSensitive"
		if Month == "May":
			if Air_Pressure <=  988.54:
				if Temperature <=  38.63:
					if Temperature <=  27.39:
						return "VeryGood"
					if Temperature >  27.39:
						if Hour <=  7:
							if Temperature <=  30.1:
								if Hour <=  2:
									return "VeryGood"
								if Hour >  2:
									if Hour <=  3:
										if Temperature <=  29.28:
											if Temperature <=  28.36:
												return "VeryGood"
											if Temperature >  28.36:
												return "Moderate"
										if Temperature >  29.28:
											return "UnhealthyForSensitive"
									if Hour >  3:
										return "Moderate"
							if Temperature >  30.1:
								return "Moderate"
						if Hour >  7:
							if Hour <=  16:
								if Location == "Pathumthani":
									return "Moderate"
								if Location == "ChiangRai":
									if Hour <=  8:
										if Relative_Humidity <=  81.44:
											return "Moderate"
										if Relative_Humidity >  81.44:
											return "VeryGood"
									if Hour >  8:
										if Relative_Humidity <=  55.99:
											if Temperature <=  35.55:
												return "Moderate"
											if Temperature >  35.55:
												return "VeryGood"
										if Relative_Humidity >  55.99:
											return "VeryGood"
								if Location == "Tak":
									if Relative_Humidity <=  63.6:
										return "Moderate"
									if Relative_Humidity >  63.6:
										return "VeryGood"
							if Hour >  16:
								if Relative_Humidity <=  74.34:
									return "Moderate"
								if Relative_Humidity >  74.34:
									if Hour <=  18:
										return "VeryGood"
									if Hour >  18:
										if Temperature <=  28.2:
											return "VeryGood"
										if Temperature >  28.2:
											if Hour <=  22:
												if Relative_Humidity <=  82.26:
													return "Moderate"
												if Relative_Humidity >  82.26:
													if Relative_Humidity <=  84.29:
														return "VeryGood"
													if Relative_Humidity >  84.29:
														return "Moderate"
											if Hour >  22:
												if Relative_Humidity <=  78.25:
													return "VeryGood"
												if Relative_Humidity >  78.25:
													return "Moderate"
				if Temperature >  38.63:
					return "VeryGood"
			if Air_Pressure >  988.54:
				if Relative_Humidity <=  66.11:
					if Hour <=  18:
						if Relative_Humidity <=  53.13:
							if Air_Pressure <=  997.73:
								return "Moderate"
							if Air_Pressure >  997.73:
								return "VeryGood"
						if Relative_Humidity >  53.13:
							if Temperature <=  37.64:
								if Location == "Pathumthani":
									if Air_Pressure <=  996.36:
										if Hour <=  10:
											if Temperature <=  32.46:
												return "Moderate"
											if Temperature >  32.46:
												return "UnhealthyForSensitive"
										if Hour >  10:
											return "Moderate"
									if Air_Pressure >  996.36:
										if Relative_Humidity <=  59.87:
											if Temperature <=  33.66:
												return "Moderate"
											if Temperature >  33.66:
												if Hour <=  11:
													if Air_Pressure <=  999.78:
														return "Moderate"
													if Air_Pressure >  999.78:
														return "VeryGood"
												if Hour >  11:
													return "VeryGood"
										if Relative_Humidity >  59.87:
											if Air_Pressure <=  1000.74:
												if Hour <=  4:
													return "VeryGood"
												if Hour >  4:
													if Hour <=  15:
														return "Moderate"
													if Hour >  15:
														return "VeryGood"
											if Air_Pressure >  1000.74:
												return "Moderate"
								if Location == "ChiangRai":
									if Temperature <=  34.19:
										return "Moderate"
									if Temperature >  34.19:
										return "UnhealthyForSensitive"
								if Location == "Tak":
									return "Moderate"
							if Temperature >  37.64:
								if Hour <=  12:
									return "Moderate"
								if Hour >  12:
									if Relative_Humidity <=  56.45:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  56.45:
										if Relative_Humidity <=  59.86:
											if Hour <=  13:
												if Temperature <=  39.22:
													return "UnhealthyForSensitive"
												if Temperature >  39.22:
													return "Moderate"
											if Hour >  13:
												return "Moderate"
										if Relative_Humidity >  59.86:
											return "UnhealthyForSensitive"
					if Hour >  18:
						if Air_Pressure <=  1010.94:
							return "Moderate"
						if Air_Pressure >  1010.94:
							return "UnhealthyForSensitive"
				if Relative_Humidity >  66.11:
					if Temperature <=  30.5:
						if Location == "Pathumthani":
							if Air_Pressure <=  1004.4:
								if Air_Pressure <=  995.77:
									return "Moderate"
								if Air_Pressure >  995.77:
									if Hour <=  3:
										return "VeryGood"
									if Hour >  3:
										return "Moderate"
							if Air_Pressure >  1004.4:
								if Relative_Humidity <=  93.68:
									if Air_Pressure <=  1006.32:
										if Relative_Humidity <=  92.84:
											if Hour <=  1:
												return "VeryGood"
											if Hour >  1:
												return "Moderate"
										if Relative_Humidity >  92.84:
											if Temperature <=  29.35:
												return "VeryGood"
											if Temperature >  29.35:
												return "UnhealthyForSensitive"
									if Air_Pressure >  1006.32:
										if Air_Pressure <=  1010.21:
											if Relative_Humidity <=  87.58:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  87.58:
												if Temperature <=  29.42:
													if Hour <=  8:
														return "UnhealthyForSensitive"
													if Hour >  8:
														return "VeryGood"
												if Temperature >  29.42:
													if Hour <=  9:
														if Relative_Humidity <=  92.58:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  92.58:
															return "Moderate"
													if Hour >  9:
														return "Moderate"
										if Air_Pressure >  1010.21:
											return "VeryGood"
								if Relative_Humidity >  93.68:
									if Hour <=  9:
										if Hour <=  7:
											if Hour <=  1:
												if Relative_Humidity <=  96.67:
													if Temperature <=  28.61:
														return "VeryGood"
													if Temperature >  28.61:
														if Relative_Humidity <=  94.47:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  94.47:
															return "Moderate"
												if Relative_Humidity >  96.67:
													return "UnhealthyForSensitive"
											if Hour >  1:
												if Temperature <=  29.73:
													if Hour <=  6:
														return "UnhealthyForSensitive"
													if Hour >  6:
														return "Moderate"
												if Temperature >  29.73:
													return "UnhealthyForSensitive"
										if Hour >  7:
											if Temperature <=  29.17:
												return "VeryGood"
											if Temperature >  29.17:
												return "Moderate"
									if Hour >  9:
										if Hour <=  14:
											return "Moderate"
										if Hour >  14:
											if Hour <=  19:
												if Relative_Humidity <=  94.49:
													return "Unhealthy"
												if Relative_Humidity >  94.49:
													return "UnhealthyForSensitive"
											if Hour >  19:
												if Relative_Humidity <=  97.57:
													return "Moderate"
												if Relative_Humidity >  97.57:
													return "UnhealthyForSensitive"
						if Location == "ChiangRai":
							if Hour <=  5:
								return "Moderate"
							if Hour >  5:
								if Relative_Humidity <=  73.85:
									return "Moderate"
								if Relative_Humidity >  73.85:
									return "UnhealthyForSensitive"
						if Location == "Tak":
							if Hour <=  5:
								return "Moderate"
							if Hour >  5:
								if Hour <=  6:
									return "UnhealthyForSensitive"
								if Hour >  6:
									return "Unhealthy"
					if Temperature >  30.5:
						if Hour <=  15:
							if Temperature <=  31.53:
								if Hour <=  2:
									if Air_Pressure <=  1006.64:
										if Relative_Humidity <=  90.76:
											return "Moderate"
										if Relative_Humidity >  90.76:
											return "UnhealthyForSensitive"
									if Air_Pressure >  1006.64:
										return "UnhealthyForSensitive"
								if Hour >  2:
									return "Moderate"
							if Temperature >  31.53:
								return "Moderate"
						if Hour >  15:
							if Air_Pressure <=  1008.42:
								if Temperature <=  31.32:
									if Relative_Humidity <=  92.44:
										return "Moderate"
									if Relative_Humidity >  92.44:
										return "UnhealthyForSensitive"
								if Temperature >  31.32:
									if Air_Pressure <=  1003.82:
										if Temperature <=  34.78:
											if Hour <=  18:
												if Air_Pressure <=  1002.73:
													return "VeryGood"
												if Air_Pressure >  1002.73:
													return "Moderate"
											if Hour >  18:
												if Air_Pressure <=  998.11:
													return "Moderate"
												if Air_Pressure >  998.11:
													return "UnhealthyForSensitive"
										if Temperature >  34.78:
											return "UnhealthyForSensitive"
									if Air_Pressure >  1003.82:
										return "Moderate"
							if Air_Pressure >  1008.42:
								if Relative_Humidity <=  68.78:
									return "Moderate"
								if Relative_Humidity >  68.78:
									if Hour <=  22:
										return "Unhealthy"
									if Hour >  22:
										return "UnhealthyForSensitive"
		if Month == "June":
			if Air_Pressure <=  986.09:
				if Temperature <=  33.49:
					if Hour <=  4:
						if Relative_Humidity <=  83.43:
							if Air_Pressure <=  982.53:
								if Location == "Pathumthani":
									return "Moderate"
								if Location == "ChiangRai":
									if Hour <=  2:
										return "Moderate"
									if Hour >  2:
										return "VeryGood"
								if Location == "Tak":
									if Hour <=  3:
										return "VeryGood"
									if Hour >  3:
										return "Moderate"
							if Air_Pressure >  982.53:
								return "VeryGood"
						if Relative_Humidity >  83.43:
							return "VeryGood"
					if Hour >  4:
						if Hour <=  8:
							if Location == "Pathumthani":
								return "Moderate"
							if Location == "ChiangRai":
								if Air_Pressure <=  982.77:
									return "VeryGood"
								if Air_Pressure >  982.77:
									if Hour <=  6:
										return "Moderate"
									if Hour >  6:
										if Relative_Humidity <=  80.15:
											return "Moderate"
										if Relative_Humidity >  80.15:
											if Temperature <=  28.25:
												return "Moderate"
											if Temperature >  28.25:
												return "VeryGood"
							if Location == "Tak":
								if Hour <=  5:
									return "VeryGood"
								if Hour >  5:
									if Hour <=  7:
										return "Moderate"
									if Hour >  7:
										return "VeryGood"
						if Hour >  8:
							if Relative_Humidity <=  74.64:
								if Hour <=  17:
									if Air_Pressure <=  979.17:
										if Location == "Pathumthani":
											return "Moderate"
										if Location == "ChiangRai":
											if Relative_Humidity <=  68.11:
												return "Moderate"
											if Relative_Humidity >  68.11:
												return "VeryGood"
										if Location == "Tak":
											return "VeryGood"
									if Air_Pressure >  979.17:
										return "VeryGood"
								if Hour >  17:
									return "Moderate"
							if Relative_Humidity >  74.64:
								return "VeryGood"
				if Temperature >  33.49:
					return "VeryGood"
			if Air_Pressure >  986.09:
				if Relative_Humidity <=  86.05:
					if Hour <=  17:
						if Location == "Pathumthani":
							return "Moderate"
						if Location == "ChiangRai":
							if Hour <=  9:
								if Hour <=  3:
									return "VeryGood"
								if Hour >  3:
									return "Moderate"
							if Hour >  9:
								if Temperature <=  32.19:
									if Relative_Humidity <=  65.26:
										return "Moderate"
									if Relative_Humidity >  65.26:
										if Temperature <=  29.92:
											if Air_Pressure <=  991.1:
												return "VeryGood"
											if Air_Pressure >  991.1:
												return "Moderate"
										if Temperature >  29.92:
											return "VeryGood"
								if Temperature >  32.19:
									return "VeryGood"
						if Location == "Tak":
							if Hour <=  2:
								return "VeryGood"
							if Hour >  2:
								if Temperature <=  32.49:
									return "Moderate"
								if Temperature >  32.49:
									return "VeryGood"
					if Hour >  17:
						if Hour <=  21:
							return "Moderate"
						if Hour >  21:
							if Temperature <=  30.96:
								if Hour <=  22:
									if Location == "Pathumthani":
										return "VeryGood"
									if Location == "ChiangRai":
										if Air_Pressure <=  994.06:
											return "VeryGood"
										if Air_Pressure >  994.06:
											return "Moderate"
									if Location == "Tak":
										return "Moderate"
								if Hour >  22:
									return "VeryGood"
							if Temperature >  30.96:
								return "Moderate"
				if Relative_Humidity >  86.05:
					if Relative_Humidity <=  97.92:
						if Temperature <=  29.2:
							if Relative_Humidity <=  96:
								if Hour <=  5:
									return "VeryGood"
								if Hour >  5:
									if Temperature <=  28.61:
										return "VeryGood"
									if Temperature >  28.61:
										if Hour <=  22:
											return "Moderate"
										if Hour >  22:
											return "VeryGood"
							if Relative_Humidity >  96:
								if Temperature <=  28.26:
									if Hour <=  2:
										return "VeryGood"
									if Hour >  2:
										if Relative_Humidity <=  96.6:
											return "VeryGood"
										if Relative_Humidity >  96.6:
											return "Moderate"
								if Temperature >  28.26:
									return "Moderate"
						if Temperature >  29.2:
							if Relative_Humidity <=  94.36:
								if Temperature <=  32.11:
									if Relative_Humidity <=  91.17:
										if Temperature <=  31.17:
											if Air_Pressure <=  1008.03:
												return "VeryGood"
											if Air_Pressure >  1008.03:
												return "Moderate"
										if Temperature >  31.17:
											return "Moderate"
									if Relative_Humidity >  91.17:
										if Hour <=  17:
											return "Moderate"
										if Hour >  17:
											if Relative_Humidity <=  93.71:
												if Relative_Humidity <=  92.46:
													return "VeryGood"
												if Relative_Humidity >  92.46:
													return "Moderate"
											if Relative_Humidity >  93.71:
												return "VeryGood"
								if Temperature >  32.11:
									return "UnhealthyForSensitive"
							if Relative_Humidity >  94.36:
								return "Moderate"
					if Relative_Humidity >  97.92:
						if Relative_Humidity <=  98.84:
							return "Moderate"
						if Relative_Humidity >  98.84:
							return "UnhealthyForSensitive"
		if Month == "July":
			if Relative_Humidity <=  77.99:
				if Hour <=  4:
					if Temperature <=  30.78:
						return "VeryGood"
					if Temperature >  30.78:
						return "Moderate"
				if Hour >  4:
					if Hour <=  7:
						if Relative_Humidity <=  76.97:
							return "Moderate"
						if Relative_Humidity >  76.97:
							if Hour <=  5:
								return "VeryGood"
							if Hour >  5:
								if Hour <=  6:
									return "Moderate"
								if Hour >  6:
									return "VeryGood"
					if Hour >  7:
						if Air_Pressure <=  1001.37:
							if Hour <=  17:
								if Relative_Humidity <=  72.14:
									return "VeryGood"
								if Relative_Humidity >  72.14:
									if Temperature <=  29:
										return "VeryGood"
									if Temperature >  29:
										if Location == "Pathumthani":
											return "Moderate"
										if Location == "ChiangRai":
											if Hour <=  15:
												if Relative_Humidity <=  75.42:
													return "VeryGood"
												if Relative_Humidity >  75.42:
													if Air_Pressure <=  988.23:
														return "VeryGood"
													if Air_Pressure >  988.23:
														return "Moderate"
											if Hour >  15:
												return "Moderate"
										if Location == "Tak":
											if Hour <=  8:
												return "VeryGood"
											if Hour >  8:
												if Relative_Humidity <=  73.05:
													return "VeryGood"
												if Relative_Humidity >  73.05:
													return "Moderate"
							if Hour >  17:
								if Temperature <=  26.65:
									return "Moderate"
								if Temperature >  26.65:
									if Hour <=  18:
										return "VeryGood"
									if Hour >  18:
										if Hour <=  19:
											return "Moderate"
										if Hour >  19:
											return "VeryGood"
						if Air_Pressure >  1001.37:
							if Hour <=  15:
								if Relative_Humidity <=  59.49:
									return "Moderate"
								if Relative_Humidity >  59.49:
									if Relative_Humidity <=  69.21:
										if Temperature <=  35.73:
											return "VeryGood"
										if Temperature >  35.73:
											if Hour <=  12:
												if Air_Pressure <=  1006.84:
													return "Moderate"
												if Air_Pressure >  1006.84:
													return "VeryGood"
											if Hour >  12:
												return "VeryGood"
									if Relative_Humidity >  69.21:
										if Air_Pressure <=  1008.33:
											return "Moderate"
										if Air_Pressure >  1008.33:
											return "VeryGood"
							if Hour >  15:
								return "Moderate"
			if Relative_Humidity >  77.99:
				if Hour <=  4:
					if Relative_Humidity <=  95.81:
						if Temperature <=  29.28:
							return "VeryGood"
						if Temperature >  29.28:
							if Air_Pressure <=  1006.25:
								if Air_Pressure <=  1003.42:
									if Relative_Humidity <=  85.41:
										return "Moderate"
									if Relative_Humidity >  85.41:
										return "VeryGood"
								if Air_Pressure >  1003.42:
									return "Moderate"
							if Air_Pressure >  1006.25:
								if Relative_Humidity <=  87.07:
									return "VeryGood"
								if Relative_Humidity >  87.07:
									if Relative_Humidity <=  93.24:
										if Temperature <=  29.84:
											return "VeryGood"
										if Temperature >  29.84:
											return "Moderate"
									if Relative_Humidity >  93.24:
										return "Moderate"
					if Relative_Humidity >  95.81:
						if Relative_Humidity <=  97.19:
							if Temperature <=  28.03:
								return "VeryGood"
							if Temperature >  28.03:
								return "Moderate"
						if Relative_Humidity >  97.19:
							return "Moderate"
				if Hour >  4:
					if Location == "Pathumthani":
						if Air_Pressure <=  1005.17:
							if Relative_Humidity <=  81.39:
								if Hour <=  13:
									if Hour <=  8:
										if Relative_Humidity <=  78.98:
											if Air_Pressure <=  990.67:
												return "Moderate"
											if Air_Pressure >  990.67:
												return "VeryGood"
										if Relative_Humidity >  78.98:
											return "Moderate"
									if Hour >  8:
										return "VeryGood"
								if Hour >  13:
									return "Moderate"
							if Relative_Humidity >  81.39:
								return "VeryGood"
						if Air_Pressure >  1005.17:
							if Relative_Humidity <=  91.55:
								if Temperature <=  30.5:
									if Air_Pressure <=  1005.99:
										return "Moderate"
									if Air_Pressure >  1005.99:
										return "VeryGood"
								if Temperature >  30.5:
									if Relative_Humidity <=  86.45:
										if Air_Pressure <=  1008.79:
											if Hour <=  18:
												if Hour <=  11:
													return "Moderate"
												if Hour >  11:
													if Temperature <=  33.28:
														if Temperature <=  31.72:
															return "VeryGood"
														if Temperature >  31.72:
															if Hour <=  17:
																if Relative_Humidity <=  81.24:
																	return "VeryGood"
																if Relative_Humidity >  81.24:
																	if Relative_Humidity <=  83.27:
																		return "Moderate"
																	if Relative_Humidity >  83.27:
																		return "VeryGood"
															if Hour >  17:
																return "Moderate"
													if Temperature >  33.28:
														return "UnhealthyForSensitive"
											if Hour >  18:
												if Air_Pressure <=  1007.92:
													return "Moderate"
												if Air_Pressure >  1007.92:
													if Hour <=  20:
														return "Moderate"
													if Hour >  20:
														return "VeryGood"
										if Air_Pressure >  1008.79:
											return "VeryGood"
									if Relative_Humidity >  86.45:
										return "Moderate"
							if Relative_Humidity >  91.55:
								if Temperature <=  29.18:
									if Relative_Humidity <=  93.1:
										return "VeryGood"
									if Relative_Humidity >  93.1:
										return "Moderate"
								if Temperature >  29.18:
									return "Moderate"
					if Location == "ChiangRai":
						return "Moderate"
					if Location == "Tak":
						if Air_Pressure <=  993.02:
							return "Moderate"
						if Air_Pressure >  993.02:
							return "VeryGood"
		if Month == "August":
			if Relative_Humidity <=  76.55:
				if Hour <=  17:
					if Hour <=  3:
						return "VeryGood"
					if Hour >  3:
						if Hour <=  8:
							if Hour <=  4:
								if Temperature <=  30.24:
									return "Moderate"
								if Temperature >  30.24:
									return "VeryGood"
							if Hour >  4:
								if Relative_Humidity <=  70.31:
									if Location == "Pathumthani":
										if Air_Pressure <=  993.29:
											if Relative_Humidity <=  67.18:
												return "Moderate"
											if Relative_Humidity >  67.18:
												if Hour <=  5:
													return "VeryGood"
												if Hour >  5:
													if Relative_Humidity <=  69.62:
														return "VeryGood"
													if Relative_Humidity >  69.62:
														return "Moderate"
										if Air_Pressure >  993.29:
											return "Moderate"
									if Location == "ChiangRai":
										return "Moderate"
									if Location == "Tak":
										if Hour <=  7:
											return "Moderate"
										if Hour >  7:
											return "VeryGood"
								if Relative_Humidity >  70.31:
									if Relative_Humidity <=  73.05:
										if Air_Pressure <=  993.59:
											if Temperature <=  30.68:
												return "Moderate"
											if Temperature >  30.68:
												return "UnhealthyForSensitive"
										if Air_Pressure >  993.59:
											return "Moderate"
									if Relative_Humidity >  73.05:
										if Air_Pressure <=  994.47:
											return "Moderate"
										if Air_Pressure >  994.47:
											return "VeryGood"
						if Hour >  8:
							if Location == "Pathumthani":
								return "VeryGood"
							if Location == "ChiangRai":
								return "VeryGood"
							if Location == "Tak":
								if Relative_Humidity <=  64.72:
									if Relative_Humidity <=  63.14:
										if Air_Pressure <=  991.76:
											if Temperature <=  32.57:
												if Hour <=  12:
													return "VeryGood"
												if Hour >  12:
													if Temperature <=  31.47:
														if Relative_Humidity <=  59.75:
															return "VeryGood"
														if Relative_Humidity >  59.75:
															if Relative_Humidity <=  61.67:
																return "Moderate"
															if Relative_Humidity >  61.67:
																return "VeryGood"
													if Temperature >  31.47:
														return "Moderate"
											if Temperature >  32.57:
												return "VeryGood"
										if Air_Pressure >  991.76:
											return "VeryGood"
									if Relative_Humidity >  63.14:
										if Hour <=  15:
											if Hour <=  10:
												return "Moderate"
											if Hour >  10:
												return "VeryGood"
										if Hour >  15:
											return "Moderate"
								if Relative_Humidity >  64.72:
									return "VeryGood"
				if Hour >  17:
					if Hour <=  22:
						if Location == "Pathumthani":
							return "Moderate"
						if Location == "ChiangRai":
							return "Moderate"
						if Location == "Tak":
							if Temperature <=  28.62:
								if Temperature <=  27.36:
									return "Moderate"
								if Temperature >  27.36:
									return "VeryGood"
							if Temperature >  28.62:
								if Air_Pressure <=  995.79:
									if Temperature <=  31.62:
										return "Moderate"
									if Temperature >  31.62:
										return "VeryGood"
								if Air_Pressure >  995.79:
									return "VeryGood"
					if Hour >  22:
						return "VeryGood"
			if Relative_Humidity >  76.55:
				if Relative_Humidity <=  91.29:
					if Hour <=  10:
						if Air_Pressure <=  1007.31:
							if Location == "Pathumthani":
								if Air_Pressure <=  1004.58:
									return "Moderate"
								if Air_Pressure >  1004.58:
									if Air_Pressure <=  1005.11:
										return "VeryGood"
									if Air_Pressure >  1005.11:
										if Relative_Humidity <=  83.65:
											return "VeryGood"
										if Relative_Humidity >  83.65:
											return "Moderate"
							if Location == "ChiangRai":
								if Hour <=  5:
									return "VeryGood"
								if Hour >  5:
									return "Moderate"
							if Location == "Tak":
								if Hour <=  5:
									return "VeryGood"
								if Hour >  5:
									return "Moderate"
						if Air_Pressure >  1007.31:
							if Relative_Humidity <=  86.75:
								return "VeryGood"
							if Relative_Humidity >  86.75:
								if Hour <=  9:
									if Air_Pressure <=  1008.42:
										return "VeryGood"
									if Air_Pressure >  1008.42:
										return "Moderate"
								if Hour >  9:
									return "Moderate"
					if Hour >  10:
						if Relative_Humidity <=  90.85:
							return "Moderate"
						if Relative_Humidity >  90.85:
							if Temperature <=  30.68:
								return "VeryGood"
							if Temperature >  30.68:
								return "Moderate"
				if Relative_Humidity >  91.29:
					if Temperature <=  28.77:
						if Relative_Humidity <=  97.84:
							return "VeryGood"
						if Relative_Humidity >  97.84:
							return "Moderate"
					if Temperature >  28.77:
						if Temperature <=  29.07:
							if Relative_Humidity <=  97.88:
								return "UnhealthyForSensitive"
							if Relative_Humidity >  97.88:
								if Hour <=  4:
									return "Moderate"
								if Hour >  4:
									return "UnhealthyForSensitive"
						if Temperature >  29.07:
							if Relative_Humidity <=  97.18:
								if Temperature <=  29.95:
									if Relative_Humidity <=  95.28:
										if Hour <=  22:
											return "Moderate"
										if Hour >  22:
											return "VeryGood"
									if Relative_Humidity >  95.28:
										return "Moderate"
								if Temperature >  29.95:
									if Hour <=  5:
										if Hour <=  1:
											return "Moderate"
										if Hour >  1:
											return "VeryGood"
									if Hour >  5:
										if Relative_Humidity <=  93.38:
											if Temperature <=  31.86:
												return "Moderate"
											if Temperature >  31.86:
												if Air_Pressure <=  1005.7:
													return "Moderate"
												if Air_Pressure >  1005.7:
													return "UnhealthyForSensitive"
										if Relative_Humidity >  93.38:
											if Hour <=  20:
												if Air_Pressure <=  1007.55:
													return "UnhealthyForSensitive"
												if Air_Pressure >  1007.55:
													if Relative_Humidity <=  95.34:
														return "Moderate"
													if Relative_Humidity >  95.34:
														return "UnhealthyForSensitive"
											if Hour >  20:
												return "Moderate"
							if Relative_Humidity >  97.18:
								if Relative_Humidity <=  99.15:
									if Temperature <=  29.63:
										if Hour <=  2:
											return "Moderate"
										if Hour >  2:
											return "UnhealthyForSensitive"
									if Temperature >  29.63:
										return "Moderate"
								if Relative_Humidity >  99.15:
									return "Moderate"
		if Month == "September":
			if Relative_Humidity <=  69.75:
				if Air_Pressure <=  1005.63:
					if Hour <=  17:
						if Temperature <=  34.76:
							if Air_Pressure <=  998.11:
								if Relative_Humidity <=  64.35:
									if Relative_Humidity <=  51.61:
										return "VeryGood"
									if Relative_Humidity >  51.61:
										if Location == "Pathumthani":
											if Temperature <=  34.69:
												return "Moderate"
											if Temperature >  34.69:
												return "UnhealthyForSensitive"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											if Temperature <=  30.12:
												return "VeryGood"
											if Temperature >  30.12:
												if Air_Pressure <=  997.05:
													return "Moderate"
												if Air_Pressure >  997.05:
													return "VeryGood"
								if Relative_Humidity >  64.35:
									if Hour <=  8:
										if Relative_Humidity <=  66.41:
											if Relative_Humidity <=  65.67:
												if Air_Pressure <=  995.52:
													return "Moderate"
												if Air_Pressure >  995.52:
													if Temperature <=  30.8:
														return "VeryGood"
													if Temperature >  30.8:
														if Hour <=  3:
															return "Moderate"
														if Hour >  3:
															if Relative_Humidity <=  64.73:
																return "Moderate"
															if Relative_Humidity >  64.73:
																return "UnhealthyForSensitive"
											if Relative_Humidity >  65.67:
												return "Moderate"
										if Relative_Humidity >  66.41:
											if Hour <=  3:
												return "VeryGood"
											if Hour >  3:
												if Location == "Pathumthani":
													if Hour <=  5:
														if Relative_Humidity <=  68.75:
															return "VeryGood"
														if Relative_Humidity >  68.75:
															return "Moderate"
													if Hour >  5:
														if Air_Pressure <=  996.54:
															return "Moderate"
														if Air_Pressure >  996.54:
															return "VeryGood"
												if Location == "ChiangRai":
													return "Moderate"
												if Location == "Tak":
													if Hour <=  7:
														return "Moderate"
													if Hour >  7:
														return "VeryGood"
									if Hour >  8:
										if Hour <=  12:
											if Air_Pressure <=  992.42:
												return "UnhealthyForSensitive"
											if Air_Pressure >  992.42:
												return "VeryGood"
										if Hour >  12:
											if Air_Pressure <=  975.75:
												return "UnhealthyForSensitive"
											if Air_Pressure >  975.75:
												return "Moderate"
							if Air_Pressure >  998.11:
								if Hour <=  7:
									if Relative_Humidity <=  69.37:
										if Hour <=  5:
											return "Moderate"
										if Hour >  5:
											if Relative_Humidity <=  65.25:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  65.25:
												return "Moderate"
									if Relative_Humidity >  69.37:
										return "UnhealthyForSensitive"
								if Hour >  7:
									if Temperature <=  31.6:
										if Hour <=  9:
											return "VeryGood"
										if Hour >  9:
											return "Moderate"
									if Temperature >  31.6:
										return "Moderate"
						if Temperature >  34.76:
							return "Moderate"
					if Hour >  17:
						if Temperature <=  31.25:
							if Hour <=  19:
								if Relative_Humidity <=  60.38:
									if Air_Pressure <=  994.5:
										return "Moderate"
									if Air_Pressure >  994.5:
										if Relative_Humidity <=  57.99:
											return "Moderate"
										if Relative_Humidity >  57.99:
											return "UnhealthyForSensitive"
								if Relative_Humidity >  60.38:
									if Relative_Humidity <=  60.89:
										return "Unhealthy"
									if Relative_Humidity >  60.89:
										if Hour <=  18:
											if Air_Pressure <=  993.6:
												return "Moderate"
											if Air_Pressure >  993.6:
												return "VeryGood"
										if Hour >  18:
											return "Moderate"
							if Hour >  19:
								if Air_Pressure <=  998:
									if Air_Pressure <=  997.11:
										if Location == "Pathumthani":
											if Relative_Humidity <=  66.21:
												if Temperature <=  30.55:
													return "VeryGood"
												if Temperature >  30.55:
													return "Moderate"
											if Relative_Humidity >  66.21:
												return "Moderate"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											if Hour <=  20:
												return "Moderate"
											if Hour >  20:
												return "VeryGood"
									if Air_Pressure >  997.11:
										return "VeryGood"
								if Air_Pressure >  998:
									return "Moderate"
						if Temperature >  31.25:
							return "Moderate"
				if Air_Pressure >  1005.63:
					if Temperature <=  31.69:
						return "UnhealthyForSensitive"
					if Temperature >  31.69:
						if Hour <=  11:
							if Temperature <=  34.69:
								if Hour <=  9:
									if Air_Pressure <=  1006.56:
										return "Moderate"
									if Air_Pressure >  1006.56:
										if Hour <=  5:
											return "VeryGood"
										if Hour >  5:
											if Hour <=  7:
												return "Moderate"
											if Hour >  7:
												if Hour <=  8:
													if Temperature <=  33.07:
														return "VeryGood"
													if Temperature >  33.07:
														return "Moderate"
												if Hour >  8:
													return "VeryGood"
								if Hour >  9:
									return "Moderate"
							if Temperature >  34.69:
								if Hour <=  9:
									if Air_Pressure <=  1007.96:
										return "Unhealthy"
									if Air_Pressure >  1007.96:
										return "VeryGood"
								if Hour >  9:
									return "VeryGood"
						if Hour >  11:
							if Air_Pressure <=  1005.83:
								return "UnhealthyForSensitive"
							if Air_Pressure >  1005.83:
								if Temperature <=  36.62:
									if Temperature <=  33.01:
										return "VeryGood"
									if Temperature >  33.01:
										if Air_Pressure <=  1008.79:
											return "Moderate"
										if Air_Pressure >  1008.79:
											return "UnhealthyForSensitive"
								if Temperature >  36.62:
									if Relative_Humidity <=  52.68:
										return "Moderate"
									if Relative_Humidity >  52.68:
										return "VeryGood"
			if Relative_Humidity >  69.75:
				if Relative_Humidity <=  97.1:
					if Location == "Pathumthani":
						if Hour <=  3:
							if Relative_Humidity <=  90.32:
								if Air_Pressure <=  1007.42:
									return "VeryGood"
								if Air_Pressure >  1007.42:
									if Relative_Humidity <=  75.77:
										if Relative_Humidity <=  72.21:
											return "VeryGood"
										if Relative_Humidity >  72.21:
											return "Moderate"
									if Relative_Humidity >  75.77:
										return "VeryGood"
							if Relative_Humidity >  90.32:
								if Relative_Humidity <=  94.21:
									return "Moderate"
								if Relative_Humidity >  94.21:
									if Air_Pressure <=  1007.69:
										if Relative_Humidity <=  96.5:
											return "Moderate"
										if Relative_Humidity >  96.5:
											return "UnhealthyForSensitive"
									if Air_Pressure >  1007.69:
										return "UnhealthyForSensitive"
						if Hour >  3:
							if Air_Pressure <=  1009.57:
								if Hour <=  11:
									if Air_Pressure <=  988.43:
										if Air_Pressure <=  981:
											return "UnhealthyForSensitive"
										if Air_Pressure >  981:
											return "VeryGood"
									if Air_Pressure >  988.43:
										if Air_Pressure <=  1007.42:
											if Temperature <=  31.5:
												if Air_Pressure <=  1007.32:
													if Temperature <=  30.06:
														if Hour <=  5:
															return "VeryGood"
														if Hour >  5:
															if Relative_Humidity <=  93.1:
																return "VeryGood"
															if Relative_Humidity >  93.1:
																return "Moderate"
													if Temperature >  30.06:
														if Hour <=  5:
															if Temperature <=  30.52:
																if Temperature <=  30.34:
																	return "Moderate"
																if Temperature >  30.34:
																	return "Unhealthy"
															if Temperature >  30.52:
																return "Moderate"
														if Hour >  5:
															if Temperature <=  30.45:
																return "Moderate"
															if Temperature >  30.45:
																if Air_Pressure <=  995.21:
																	return "Moderate"
																if Air_Pressure >  995.21:
																	return "VeryGood"
												if Air_Pressure >  1007.32:
													return "Unhealthy"
											if Temperature >  31.5:
												return "Unhealthy"
										if Air_Pressure >  1007.42:
											if Relative_Humidity <=  76.14:
												if Relative_Humidity <=  71.28:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  71.28:
													return "VeryGood"
											if Relative_Humidity >  76.14:
												if Temperature <=  34.48:
													if Hour <=  9:
														return "Moderate"
													if Hour >  9:
														return "VeryGood"
												if Temperature >  34.48:
													return "Moderate"
								if Hour >  11:
									if Relative_Humidity <=  92.25:
										if Hour <=  19:
											if Hour <=  14:
												if Air_Pressure <=  995.39:
													return "UnhealthyForSensitive"
												if Air_Pressure >  995.39:
													return "Moderate"
											if Hour >  14:
												if Temperature <=  34.67:
													if Relative_Humidity <=  73.27:
														if Hour <=  16:
															return "VeryGood"
														if Hour >  16:
															return "UnhealthyForSensitive"
													if Relative_Humidity >  73.27:
														if Hour <=  18:
															if Hour <=  15:
																return "Moderate"
															if Hour >  15:
																if Relative_Humidity <=  84.46:
																	if Air_Pressure <=  1004.96:
																		return "VeryGood"
																	if Air_Pressure >  1004.96:
																		return "Moderate"
																if Relative_Humidity >  84.46:
																	if Temperature <=  32.18:
																		return "VeryGood"
																	if Temperature >  32.18:
																		return "UnhealthyForSensitive"
														if Hour >  18:
															return "Moderate"
												if Temperature >  34.67:
													return "Moderate"
										if Hour >  19:
											if Temperature <=  30.96:
												return "Moderate"
											if Temperature >  30.96:
												if Air_Pressure <=  1007.36:
													return "VeryGood"
												if Air_Pressure >  1007.36:
													if Hour <=  20:
														return "Moderate"
													if Hour >  20:
														if Relative_Humidity <=  86.9:
															return "VeryGood"
														if Relative_Humidity >  86.9:
															if Relative_Humidity <=  90.56:
																return "Moderate"
															if Relative_Humidity >  90.56:
																return "VeryGood"
									if Relative_Humidity >  92.25:
										if Temperature <=  31.29:
											return "Unhealthy"
										if Temperature >  31.29:
											return "UnhealthyForSensitive"
							if Air_Pressure >  1009.57:
								if Temperature <=  33.87:
									if Hour <=  21:
										return "UnhealthyForSensitive"
									if Hour >  21:
										return "Moderate"
								if Temperature >  33.87:
									return "VeryGood"
					if Location == "ChiangRai":
						return "Moderate"
					if Location == "Tak":
						return "Moderate"
				if Relative_Humidity >  97.1:
					if Relative_Humidity <=  98.75:
						return "UnhealthyForSensitive"
					if Relative_Humidity >  98.75:
						return "Unhealthy"
		if Month == "October":
			if Air_Pressure <=  1012.78:
				if Relative_Humidity <=  44.29:
					if Location == "Pathumthani":
						if Temperature <=  38.57:
							return "Unhealthy"
						if Temperature >  38.57:
							if Air_Pressure <=  1009.4:
								return "Moderate"
							if Air_Pressure >  1009.4:
								return "UnhealthyForSensitive"
					if Location == "ChiangRai":
						return "Unhealthy"
					if Location == "Tak":
						return "Moderate"
				if Relative_Humidity >  44.29:
					if Temperature <=  35.51:
						if Relative_Humidity <=  56.03:
							if Hour <=  17:
								if Hour <=  5:
									return "Unhealthy"
								if Hour >  5:
									if Temperature <=  33.32:
										if Temperature <=  31.32:
											return "UnhealthyForSensitive"
										if Temperature >  31.32:
											if Hour <=  15:
												if Location == "Pathumthani":
													if Temperature <=  31.91:
														return "Moderate"
													if Temperature >  31.91:
														if Air_Pressure <=  998.43:
															return "UnhealthyForSensitive"
														if Air_Pressure >  998.43:
															if Temperature <=  32.26:
																return "UnhealthyForSensitive"
															if Temperature >  32.26:
																return "Moderate"
												if Location == "ChiangRai":
													return "UnhealthyForSensitive"
												if Location == "Tak":
													if Relative_Humidity <=  51.44:
														if Hour <=  11:
															if Relative_Humidity <=  50.45:
																return "UnhealthyForSensitive"
															if Relative_Humidity >  50.45:
																return "VeryGood"
														if Hour >  11:
															if Air_Pressure <=  996.5:
																if Temperature <=  33.03:
																	return "UnhealthyForSensitive"
																if Temperature >  33.03:
																	if Relative_Humidity <=  48.83:
																		return "UnhealthyForSensitive"
																	if Relative_Humidity >  48.83:
																		return "Moderate"
															if Air_Pressure >  996.5:
																return "Moderate"
													if Relative_Humidity >  51.44:
														return "Moderate"
											if Hour >  15:
												if Location == "Pathumthani":
													return "Moderate"
												if Location == "ChiangRai":
													return "Moderate"
												if Location == "Tak":
													if Hour <=  16:
														return "Moderate"
													if Hour >  16:
														if Air_Pressure <=  997.23:
															return "UnhealthyForSensitive"
														if Air_Pressure >  997.23:
															return "Moderate"
									if Temperature >  33.32:
										if Temperature <=  35.11:
											if Location == "Pathumthani":
												if Hour <=  11:
													if Air_Pressure <=  983.62:
														return "VeryGood"
													if Air_Pressure >  983.62:
														return "UnhealthyForSensitive"
												if Hour >  11:
													if Temperature <=  33.5:
														if Temperature <=  33.44:
															return "Moderate"
														if Temperature >  33.44:
															return "VeryGood"
													if Temperature >  33.5:
														return "Moderate"
											if Location == "ChiangRai":
												return "Moderate"
											if Location == "Tak":
												if Air_Pressure <=  996.72:
													if Air_Pressure <=  995.26:
														return "Moderate"
													if Air_Pressure >  995.26:
														return "UnhealthyForSensitive"
												if Air_Pressure >  996.72:
													return "Moderate"
										if Temperature >  35.11:
											if Hour <=  14:
												if Relative_Humidity <=  52.51:
													return "Moderate"
												if Relative_Humidity >  52.51:
													return "UnhealthyForSensitive"
											if Hour >  14:
												if Relative_Humidity <=  50.66:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  50.66:
													return "VeryGood"
							if Hour >  17:
								if Relative_Humidity <=  55.23:
									if Hour <=  19:
										if Relative_Humidity <=  51.84:
											return "Unhealthy"
										if Relative_Humidity >  51.84:
											if Air_Pressure <=  1009.93:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1009.93:
												return "Unhealthy"
									if Hour >  19:
										if Air_Pressure <=  998.98:
											if Temperature <=  30.66:
												return "UnhealthyForSensitive"
											if Temperature >  30.66:
												if Relative_Humidity <=  53.57:
													return "Unhealthy"
												if Relative_Humidity >  53.57:
													if Relative_Humidity <=  54.04:
														return "UnhealthyForSensitive"
													if Relative_Humidity >  54.04:
														return "Unhealthy"
										if Air_Pressure >  998.98:
											if Air_Pressure <=  1006.13:
												return "UnhealthyForSensitive"
											if Air_Pressure >  1006.13:
												return "Unhealthy"
								if Relative_Humidity >  55.23:
									if Hour <=  18:
										return "UnhealthyForSensitive"
									if Hour >  18:
										if Hour <=  21:
											if Location == "Pathumthani":
												if Air_Pressure <=  999.69:
													return "UnhealthyForSensitive"
												if Air_Pressure >  999.69:
													return "Moderate"
											if Location == "ChiangRai":
												return "Moderate"
											if Location == "Tak":
												return "Moderate"
										if Hour >  21:
											return "UnhealthyForSensitive"
						if Relative_Humidity >  56.03:
							if Hour <=  8:
								if Relative_Humidity <=  66.18:
									if Air_Pressure <=  1006.83:
										if Air_Pressure <=  983.81:
											if Relative_Humidity <=  60.32:
												return "Unhealthy"
											if Relative_Humidity >  60.32:
												return "VeryGood"
										if Air_Pressure >  983.81:
											if Relative_Humidity <=  61.76:
												if Temperature <=  31.74:
													if Temperature <=  29.35:
														return "UnhealthyForSensitive"
													if Temperature >  29.35:
														if Location == "Pathumthani":
															if Hour <=  5:
																return "Unhealthy"
															if Hour >  5:
																return "UnhealthyForSensitive"
														if Location == "ChiangRai":
															return "Unhealthy"
														if Location == "Tak":
															if Temperature <=  31.4:
																return "Unhealthy"
															if Temperature >  31.4:
																return "UnhealthyForSensitive"
												if Temperature >  31.74:
													return "UnhealthyForSensitive"
											if Relative_Humidity >  61.76:
												if Hour <=  4:
													if Air_Pressure <=  984.55:
														return "UnhealthyForSensitive"
													if Air_Pressure >  984.55:
														return "Moderate"
												if Hour >  4:
													if Relative_Humidity <=  64.84:
														if Temperature <=  32.5:
															return "UnhealthyForSensitive"
														if Temperature >  32.5:
															return "Moderate"
													if Relative_Humidity >  64.84:
														if Location == "Pathumthani":
															if Temperature <=  31.21:
																if Air_Pressure <=  998.14:
																	return "Moderate"
																if Air_Pressure >  998.14:
																	if Temperature <=  31.05:
																		return "Unhealthy"
																	if Temperature >  31.05:
																		return "Moderate"
															if Temperature >  31.21:
																if Temperature <=  32.41:
																	if Air_Pressure <=  998.98:
																		return "Unhealthy"
																	if Air_Pressure >  998.98:
																		return "UnhealthyForSensitive"
																if Temperature >  32.41:
																	return "Moderate"
														if Location == "ChiangRai":
															return "Moderate"
														if Location == "Tak":
															if Temperature <=  31.39:
																return "UnhealthyForSensitive"
															if Temperature >  31.39:
																if Air_Pressure <=  1000.36:
																	return "Moderate"
																if Air_Pressure >  1000.36:
																	return "UnhealthyForSensitive"
									if Air_Pressure >  1006.83:
										if Air_Pressure <=  1010.56:
											return "VeryGood"
										if Air_Pressure >  1010.56:
											if Relative_Humidity <=  63.56:
												if Air_Pressure <=  1011.77:
													return "UnhealthyForSensitive"
												if Air_Pressure >  1011.77:
													return "Unhealthy"
											if Relative_Humidity >  63.56:
												if Hour <=  1:
													return "VeryGood"
												if Hour >  1:
													if Relative_Humidity <=  65.3:
														return "Moderate"
													if Relative_Humidity >  65.3:
														return "UnhealthyForSensitive"
								if Relative_Humidity >  66.18:
									if Relative_Humidity <=  75.38:
										if Temperature <=  32.19:
											if Temperature <=  29.92:
												if Relative_Humidity <=  74.56:
													if Air_Pressure <=  980.59:
														if Relative_Humidity <=  68.63:
															return "VeryGood"
														if Relative_Humidity >  68.63:
															return "Moderate"
													if Air_Pressure >  980.59:
														return "VeryGood"
												if Relative_Humidity >  74.56:
													return "Moderate"
											if Temperature >  29.92:
												if Air_Pressure <=  997.98:
													if Temperature <=  31.18:
														return "Moderate"
													if Temperature >  31.18:
														if Relative_Humidity <=  68.72:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  68.72:
															return "Unhealthy"
												if Air_Pressure >  997.98:
													if Relative_Humidity <=  70.98:
														if Temperature <=  30.59:
															return "VeryGood"
														if Temperature >  30.59:
															if Air_Pressure <=  1011.47:
																if Air_Pressure <=  1005.94:
																	return "Moderate"
																if Air_Pressure >  1005.94:
																	if Relative_Humidity <=  68.84:
																		return "VeryGood"
																	if Relative_Humidity >  68.84:
																		return "Moderate"
															if Air_Pressure >  1011.47:
																if Temperature <=  31.13:
																	return "UnhealthyForSensitive"
																if Temperature >  31.13:
																	return "Moderate"
													if Relative_Humidity >  70.98:
														if Air_Pressure <=  1007.71:
															if Temperature <=  30.5:
																if Location == "Pathumthani":
																	return "Moderate"
																if Location == "ChiangRai":
																	return "Moderate"
																if Location == "Tak":
																	return "VeryGood"
															if Temperature >  30.5:
																return "Moderate"
														if Air_Pressure >  1007.71:
															if Relative_Humidity <=  72.09:
																return "Moderate"
															if Relative_Humidity >  72.09:
																if Relative_Humidity <=  74.77:
																	if Relative_Humidity <=  73.07:
																		return "UnhealthyForSensitive"
																	if Relative_Humidity >  73.07:
																		if Relative_Humidity <=  74.03:
																			return "Moderate"
																		if Relative_Humidity >  74.03:
																			return "UnhealthyForSensitive"
																if Relative_Humidity >  74.77:
																	return "Moderate"
										if Temperature >  32.19:
											if Relative_Humidity <=  70.65:
												if Temperature <=  32.9:
													if Hour <=  6:
														if Hour <=  1:
															return "Moderate"
														if Hour >  1:
															return "UnhealthyForSensitive"
													if Hour >  6:
														return "Moderate"
												if Temperature >  32.9:
													return "UnhealthyForSensitive"
											if Relative_Humidity >  70.65:
												return "Unhealthy"
									if Relative_Humidity >  75.38:
										if Relative_Humidity <=  80.31:
											if Hour <=  2:
												if Air_Pressure <=  966.5:
													return "Moderate"
												if Air_Pressure >  966.5:
													return "Unhealthy"
											if Hour >  2:
												if Relative_Humidity <=  79.4:
													if Hour <=  4:
														return "UnhealthyForSensitive"
													if Hour >  4:
														return "Moderate"
												if Relative_Humidity >  79.4:
													return "Moderate"
										if Relative_Humidity >  80.31:
											return "UnhealthyForSensitive"
							if Hour >  8:
								if Temperature <=  32.22:
									if Location == "Pathumthani":
										if Relative_Humidity <=  62.89:
											if Air_Pressure <=  983.88:
												if Hour <=  21:
													return "VeryGood"
												if Hour >  21:
													return "UnhealthyForSensitive"
											if Air_Pressure >  983.88:
												if Air_Pressure <=  1004.96:
													return "Moderate"
												if Air_Pressure >  1004.96:
													return "VeryGood"
										if Relative_Humidity >  62.89:
											if Relative_Humidity <=  70.67:
												if Hour <=  21:
													return "Moderate"
												if Hour >  21:
													if Air_Pressure <=  999.71:
														if Temperature <=  31.59:
															if Air_Pressure <=  908.19:
																return "UnhealthyForSensitive"
															if Air_Pressure >  908.19:
																return "VeryGood"
														if Temperature >  31.59:
															return "UnhealthyForSensitive"
													if Air_Pressure >  999.71:
														return "Moderate"
											if Relative_Humidity >  70.67:
												if Temperature <=  30.51:
													if Relative_Humidity <=  78.39:
														if Air_Pressure <=  994.12:
															if Temperature <=  28.82:
																if Hour <=  20:
																	return "VeryGood"
																if Hour >  20:
																	if Temperature <=  27.93:
																		return "Moderate"
																	if Temperature >  27.93:
																		return "VeryGood"
															if Temperature >  28.82:
																if Hour <=  19:
																	return "Moderate"
																if Hour >  19:
																	return "UnhealthyForSensitive"
														if Air_Pressure >  994.12:
															if Air_Pressure <=  1009.26:
																return "VeryGood"
															if Air_Pressure >  1009.26:
																return "Moderate"
													if Relative_Humidity >  78.39:
														return "Moderate"
												if Temperature >  30.51:
													if Air_Pressure <=  1002.49:
														if Air_Pressure <=  993.43:
															return "UnhealthyForSensitive"
														if Air_Pressure >  993.43:
															return "VeryGood"
													if Air_Pressure >  1002.49:
														if Air_Pressure <=  1007.75:
															return "Moderate"
														if Air_Pressure >  1007.75:
															if Relative_Humidity <=  74.08:
																if Hour <=  21:
																	return "UnhealthyForSensitive"
																if Hour >  21:
																	return "Moderate"
															if Relative_Humidity >  74.08:
																return "UnhealthyForSensitive"
									if Location == "ChiangRai":
										return "Moderate"
									if Location == "Tak":
										if Relative_Humidity <=  69.07:
											if Hour <=  18:
												if Relative_Humidity <=  58.11:
													if Temperature <=  31.65:
														if Temperature <=  31.44:
															return "Moderate"
														if Temperature >  31.44:
															return "UnhealthyForSensitive"
													if Temperature >  31.65:
														return "Moderate"
												if Relative_Humidity >  58.11:
													return "Moderate"
											if Hour >  18:
												if Air_Pressure <=  999.99:
													if Hour <=  22:
														return "UnhealthyForSensitive"
													if Hour >  22:
														if Temperature <=  30.79:
															return "UnhealthyForSensitive"
														if Temperature >  30.79:
															return "Moderate"
												if Air_Pressure >  999.99:
													return "Moderate"
										if Relative_Humidity >  69.07:
											if Hour <=  17:
												return "VeryGood"
											if Hour >  17:
												if Hour <=  20:
													return "Moderate"
												if Hour >  20:
													if Air_Pressure <=  1001.26:
														return "VeryGood"
													if Air_Pressure >  1001.26:
														return "Moderate"
								if Temperature >  32.22:
									if Relative_Humidity <=  63.76:
										if Air_Pressure <=  1008.6:
											if Air_Pressure <=  1000.67:
												if Hour <=  13:
													if Hour <=  10:
														if Air_Pressure <=  999.5:
															return "Moderate"
														if Air_Pressure >  999.5:
															if Location == "Pathumthani":
																if Relative_Humidity <=  57.77:
																	return "Moderate"
																if Relative_Humidity >  57.77:
																	return "UnhealthyForSensitive"
															if Location == "ChiangRai":
																return "UnhealthyForSensitive"
															if Location == "Tak":
																return "UnhealthyForSensitive"
													if Hour >  10:
														if Location == "Pathumthani":
															if Temperature <=  32.81:
																return "VeryGood"
															if Temperature >  32.81:
																return "Moderate"
														if Location == "ChiangRai":
															return "Moderate"
														if Location == "Tak":
															if Relative_Humidity <=  58.4:
																return "Moderate"
															if Relative_Humidity >  58.4:
																return "VeryGood"
												if Hour >  13:
													if Hour <=  19:
														return "Moderate"
													if Hour >  19:
														if Temperature <=  32.48:
															return "UnhealthyForSensitive"
														if Temperature >  32.48:
															if Temperature <=  33.76:
																return "Moderate"
															if Temperature >  33.76:
																if Relative_Humidity <=  57.39:
																	return "UnhealthyForSensitive"
																if Relative_Humidity >  57.39:
																	return "Moderate"
											if Air_Pressure >  1000.67:
												return "Moderate"
										if Air_Pressure >  1008.6:
											if Hour <=  20:
												if Hour <=  12:
													if Relative_Humidity <=  58.76:
														return "VeryGood"
													if Relative_Humidity >  58.76:
														if Temperature <=  34.31:
															if Hour <=  9:
																return "VeryGood"
															if Hour >  9:
																return "Moderate"
														if Temperature >  34.31:
															return "Moderate"
												if Hour >  12:
													if Hour <=  13:
														return "UnhealthyForSensitive"
													if Hour >  13:
														if Hour <=  18:
															return "Moderate"
														if Hour >  18:
															if Air_Pressure <=  1011.74:
																return "Moderate"
															if Air_Pressure >  1011.74:
																return "UnhealthyForSensitive"
											if Hour >  20:
												if Temperature <=  33.8:
													return "VeryGood"
												if Temperature >  33.8:
													return "UnhealthyForSensitive"
									if Relative_Humidity >  63.76:
										return "Moderate"
					if Temperature >  35.51:
						if Air_Pressure <=  1003.61:
							return "Moderate"
						if Air_Pressure >  1003.61:
							if Relative_Humidity <=  55.73:
								if Air_Pressure <=  1011.06:
									if Hour <=  16:
										if Air_Pressure <=  1009.38:
											if Relative_Humidity <=  54.01:
												return "VeryGood"
											if Relative_Humidity >  54.01:
												return "Moderate"
										if Air_Pressure >  1009.38:
											if Hour <=  14:
												if Relative_Humidity <=  47.16:
													if Relative_Humidity <=  46.33:
														return "Moderate"
													if Relative_Humidity >  46.33:
														return "Unhealthy"
												if Relative_Humidity >  47.16:
													if Air_Pressure <=  1009.85:
														return "Moderate"
													if Air_Pressure >  1009.85:
														return "VeryGood"
											if Hour >  14:
												return "Moderate"
									if Hour >  16:
										if Relative_Humidity <=  52.83:
											return "VeryGood"
										if Relative_Humidity >  52.83:
											return "Moderate"
								if Air_Pressure >  1011.06:
									if Relative_Humidity <=  50.31:
										if Hour <=  13:
											return "UnhealthyForSensitive"
										if Hour >  13:
											return "Moderate"
									if Relative_Humidity >  50.31:
										if Air_Pressure <=  1011.89:
											if Hour <=  11:
												return "Moderate"
											if Hour >  11:
												return "VeryGood"
										if Air_Pressure >  1011.89:
											return "VeryGood"
							if Relative_Humidity >  55.73:
								if Relative_Humidity <=  57.24:
									return "Moderate"
								if Relative_Humidity >  57.24:
									if Relative_Humidity <=  57.42:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  57.42:
										return "Moderate"
			if Air_Pressure >  1012.78:
				if Relative_Humidity <=  56.37:
					if Temperature <=  35.7:
						return "Unhealthy"
					if Temperature >  35.7:
						if Relative_Humidity <=  47.95:
							return "Unhealthy"
						if Relative_Humidity >  47.95:
							return "UnhealthyForSensitive"
				if Relative_Humidity >  56.37:
					if Hour <=  3:
						if Relative_Humidity <=  71.47:
							if Temperature <=  32.45:
								return "Unhealthy"
							if Temperature >  32.45:
								return "VeryGood"
						if Relative_Humidity >  71.47:
							return "VeryGood"
					if Hour >  3:
						if Relative_Humidity <=  71.37:
							if Temperature <=  32.29:
								if Relative_Humidity <=  69.06:
									return "Unhealthy"
								if Relative_Humidity >  69.06:
									if Hour <=  6:
										return "UnhealthyForSensitive"
									if Hour >  6:
										return "Moderate"
							if Temperature >  32.29:
								if Air_Pressure <=  1014.99:
									if Hour <=  10:
										if Temperature <=  33.37:
											return "UnhealthyForSensitive"
										if Temperature >  33.37:
											return "Moderate"
									if Hour >  10:
										return "UnhealthyForSensitive"
								if Air_Pressure >  1014.99:
									return "UnhealthyForSensitive"
						if Relative_Humidity >  71.37:
							if Temperature <=  30.81:
								return "VeryGood"
							if Temperature >  30.81:
								return "Moderate"
		if Month == "November":
			if Temperature <=  30.37:
				if Relative_Humidity <=  63.01:
					if Hour <=  11:
						if Hour <=  4:
							if Temperature <=  28.35:
								return "Unhealthy"
							if Temperature >  28.35:
								if Relative_Humidity <=  57.76:
									if Hour <=  3:
										if Temperature <=  28.8:
											return "Moderate"
										if Temperature >  28.8:
											if Relative_Humidity <=  57.25:
												if Air_Pressure <=  1000.83:
													if Hour <=  1:
														if Temperature <=  29.86:
															return "Unhealthy"
														if Temperature >  29.86:
															if Relative_Humidity <=  52.71:
																return "UnhealthyForSensitive"
															if Relative_Humidity >  52.71:
																return "Unhealthy"
													if Hour >  1:
														if Air_Pressure <=  999.51:
															return "UnhealthyForSensitive"
														if Air_Pressure >  999.51:
															if Relative_Humidity <=  54.53:
																return "UnhealthyForSensitive"
															if Relative_Humidity >  54.53:
																return "Unhealthy"
												if Air_Pressure >  1000.83:
													return "UnhealthyForSensitive"
											if Relative_Humidity >  57.25:
												return "Moderate"
									if Hour >  3:
										if Location == "Pathumthani":
											if Temperature <=  29.61:
												return "UnhealthyForSensitive"
											if Temperature >  29.61:
												return "Unhealthy"
										if Location == "ChiangRai":
											return "Unhealthy"
										if Location == "Tak":
											return "Unhealthy"
								if Relative_Humidity >  57.76:
									if Air_Pressure <=  998.63:
										if Air_Pressure <=  992.54:
											if Air_Pressure <=  984.7:
												return "Moderate"
											if Air_Pressure >  984.7:
												return "UnhealthyForSensitive"
										if Air_Pressure >  992.54:
											return "Moderate"
									if Air_Pressure >  998.63:
										return "UnhealthyForSensitive"
						if Hour >  4:
							if Relative_Humidity <=  45:
								return "UnhealthyForSensitive"
							if Relative_Humidity >  45:
								if Relative_Humidity <=  59.85:
									return "Unhealthy"
								if Relative_Humidity >  59.85:
									if Temperature <=  28.93:
										return "UnhealthyForSensitive"
									if Temperature >  28.93:
										if Location == "Pathumthani":
											if Temperature <=  29.84:
												return "UnhealthyForSensitive"
											if Temperature >  29.84:
												return "Unhealthy"
										if Location == "ChiangRai":
											return "Unhealthy"
										if Location == "Tak":
											if Temperature <=  30.14:
												return "Unhealthy"
											if Temperature >  30.14:
												return "UnhealthyForSensitive"
					if Hour >  11:
						return "UnhealthyForSensitive"
				if Relative_Humidity >  63.01:
					if Air_Pressure <=  989.31:
						return "Moderate"
					if Air_Pressure >  989.31:
						if Hour <=  5:
							if Temperature <=  30.22:
								if Hour <=  4:
									return "Moderate"
								if Hour >  4:
									return "UnhealthyForSensitive"
							if Temperature >  30.22:
								return "Unhealthy"
						if Hour >  5:
							if Relative_Humidity <=  66.38:
								if Hour <=  6:
									if Temperature <=  30.03:
										return "UnhealthyForSensitive"
									if Temperature >  30.03:
										return "Unhealthy"
								if Hour >  6:
									return "Unhealthy"
							if Relative_Humidity >  66.38:
								return "UnhealthyForSensitive"
			if Temperature >  30.37:
				if Air_Pressure <=  1008.25:
					if Temperature <=  32.89:
						if Relative_Humidity <=  70.6:
							if Air_Pressure <=  999.14:
								if Hour <=  4:
									if Relative_Humidity <=  55.69:
										return "Unhealthy"
									if Relative_Humidity >  55.69:
										if Location == "Pathumthani":
											if Hour <=  0:
												return "Moderate"
											if Hour >  0:
												if Temperature <=  31.14:
													if Hour <=  3:
														return "Moderate"
													if Hour >  3:
														return "UnhealthyForSensitive"
												if Temperature >  31.14:
													if Temperature <=  31.61:
														return "UnhealthyForSensitive"
													if Temperature >  31.61:
														return "Moderate"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											return "Moderate"
								if Hour >  4:
									if Hour <=  6:
										if Air_Pressure <=  991.23:
											return "Unhealthy"
										if Air_Pressure >  991.23:
											if Location == "Pathumthani":
												if Temperature <=  31.04:
													return "Moderate"
												if Temperature >  31.04:
													return "UnhealthyForSensitive"
											if Location == "ChiangRai":
												return "UnhealthyForSensitive"
											if Location == "Tak":
												if Relative_Humidity <=  63.82:
													return "Unhealthy"
												if Relative_Humidity >  63.82:
													return "UnhealthyForSensitive"
									if Hour >  6:
										if Location == "Pathumthani":
											return "Moderate"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											if Hour <=  17:
												return "Moderate"
											if Hour >  17:
												if Relative_Humidity <=  54.22:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  54.22:
													return "Moderate"
							if Air_Pressure >  999.14:
								if Air_Pressure <=  1001.12:
									if Relative_Humidity <=  52.17:
										if Temperature <=  31.26:
											if Hour <=  19:
												return "Moderate"
											if Hour >  19:
												return "Unhealthy"
										if Temperature >  31.26:
											if Relative_Humidity <=  51.68:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  51.68:
												return "Moderate"
									if Relative_Humidity >  52.17:
										if Location == "Pathumthani":
											if Relative_Humidity <=  54.19:
												return "Moderate"
											if Relative_Humidity >  54.19:
												return "UnhealthyForSensitive"
										if Location == "ChiangRai":
											return "UnhealthyForSensitive"
										if Location == "Tak":
											return "UnhealthyForSensitive"
								if Air_Pressure >  1001.12:
									if Location == "Pathumthani":
										if Temperature <=  31.01:
											if Relative_Humidity <=  51.99:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  51.99:
												return "Unhealthy"
										if Temperature >  31.01:
											return "UnhealthyForSensitive"
									if Location == "ChiangRai":
										return "UnhealthyForSensitive"
									if Location == "Tak":
										if Hour <=  20:
											if Temperature <=  31.33:
												if Relative_Humidity <=  64.78:
													return "UnhealthyForSensitive"
												if Relative_Humidity >  64.78:
													return "Moderate"
											if Temperature >  31.33:
												return "Moderate"
										if Hour >  20:
											if Temperature <=  31.33:
												return "UnhealthyForSensitive"
											if Temperature >  31.33:
												return "Unhealthy"
						if Relative_Humidity >  70.6:
							return "Unhealthy"
					if Temperature >  32.89:
						if Relative_Humidity <=  38.07:
							return "Unhealthy"
						if Relative_Humidity >  38.07:
							if Hour <=  16:
								if Air_Pressure <=  1000.68:
									return "Moderate"
								if Air_Pressure >  1000.68:
									if Location == "Pathumthani":
										if Relative_Humidity <=  47.98:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  47.98:
											if Relative_Humidity <=  54.87:
												return "Moderate"
											if Relative_Humidity >  54.87:
												return "UnhealthyForSensitive"
									if Location == "ChiangRai":
										return "Moderate"
									if Location == "Tak":
										if Air_Pressure <=  1001.04:
											return "UnhealthyForSensitive"
										if Air_Pressure >  1001.04:
											return "Moderate"
							if Hour >  16:
								if Air_Pressure <=  982.35:
									if Relative_Humidity <=  55.87:
										if Air_Pressure <=  981.24:
											return "Moderate"
										if Air_Pressure >  981.24:
											return "VeryGood"
									if Relative_Humidity >  55.87:
										return "Unhealthy"
								if Air_Pressure >  982.35:
									if Temperature <=  33.84:
										if Air_Pressure <=  1000.84:
											return "Moderate"
										if Air_Pressure >  1000.84:
											if Relative_Humidity <=  57.12:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  57.12:
												return "Unhealthy"
									if Temperature >  33.84:
										if Relative_Humidity <=  50.02:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  50.02:
											if Relative_Humidity <=  54.09:
												return "Moderate"
											if Relative_Humidity >  54.09:
												if Temperature <=  35.16:
													return "UnhealthyForSensitive"
												if Temperature >  35.16:
													return "Moderate"
				if Air_Pressure >  1008.25:
					if Relative_Humidity <=  45.18:
						return "Unhealthy"
					if Relative_Humidity >  45.18:
						if Temperature <=  34.72:
							if Relative_Humidity <=  56.69:
								if Hour <=  18:
									if Relative_Humidity <=  54.01:
										if Hour <=  12:
											if Temperature <=  34.28:
												if Hour <=  11:
													if Relative_Humidity <=  51.09:
														return "Unhealthy"
													if Relative_Humidity >  51.09:
														if Temperature <=  32.54:
															return "Unhealthy"
														if Temperature >  32.54:
															return "Moderate"
												if Hour >  11:
													return "Moderate"
											if Temperature >  34.28:
												return "UnhealthyForSensitive"
										if Hour >  12:
											return "UnhealthyForSensitive"
									if Relative_Humidity >  54.01:
										if Air_Pressure <=  1011.8:
											return "UnhealthyForSensitive"
										if Air_Pressure >  1011.8:
											return "Moderate"
								if Hour >  18:
									return "Unhealthy"
							if Relative_Humidity >  56.69:
								if Relative_Humidity <=  70.7:
									if Hour <=  19:
										if Hour <=  9:
											if Air_Pressure <=  1009.06:
												if Hour <=  3:
													return "Moderate"
												if Hour >  3:
													return "VeryGood"
											if Air_Pressure >  1009.06:
												if Temperature <=  31.14:
													if Air_Pressure <=  1010.44:
														if Relative_Humidity <=  59.93:
															return "Unhealthy"
														if Relative_Humidity >  59.93:
															if Relative_Humidity <=  68.24:
																if Relative_Humidity <=  62.29:
																	return "Moderate"
																if Relative_Humidity >  62.29:
																	return "VeryGood"
															if Relative_Humidity >  68.24:
																return "Moderate"
													if Air_Pressure >  1010.44:
														return "UnhealthyForSensitive"
												if Temperature >  31.14:
													if Hour <=  1:
														if Air_Pressure <=  1010.58:
															return "Unhealthy"
														if Air_Pressure >  1010.58:
															return "Moderate"
													if Hour >  1:
														if Temperature <=  32.56:
															return "Moderate"
														if Temperature >  32.56:
															if Relative_Humidity <=  61.18:
																return "Moderate"
															if Relative_Humidity >  61.18:
																if Temperature <=  33.32:
																	return "Moderate"
																if Temperature >  33.32:
																	return "Unhealthy"
										if Hour >  9:
											return "Moderate"
									if Hour >  19:
										if Air_Pressure <=  1010.28:
											return "Unhealthy"
										if Air_Pressure >  1010.28:
											if Hour <=  21:
												if Temperature <=  34.19:
													return "Moderate"
												if Temperature >  34.19:
													return "UnhealthyForSensitive"
											if Hour >  21:
												if Temperature <=  32:
													return "Moderate"
												if Temperature >  32:
													if Air_Pressure <=  1011.37:
														return "Unhealthy"
													if Air_Pressure >  1011.37:
														return "Moderate"
								if Relative_Humidity >  70.7:
									if Temperature <=  31.16:
										if Air_Pressure <=  1009.63:
											return "UnhealthyForSensitive"
										if Air_Pressure >  1009.63:
											return "Moderate"
									if Temperature >  31.16:
										if Air_Pressure <=  1010.67:
											return "Unhealthy"
										if Air_Pressure >  1010.67:
											return "Moderate"
						if Temperature >  34.72:
							if Relative_Humidity <=  56.46:
								if Relative_Humidity <=  54.22:
									if Relative_Humidity <=  47.73:
										if Relative_Humidity <=  46.53:
											if Temperature <=  36.78:
												return "UnhealthyForSensitive"
											if Temperature >  36.78:
												return "VeryGood"
										if Relative_Humidity >  46.53:
											if Hour <=  12:
												return "Moderate"
											if Hour >  12:
												return "UnhealthyForSensitive"
									if Relative_Humidity >  47.73:
										return "Moderate"
								if Relative_Humidity >  54.22:
									return "UnhealthyForSensitive"
							if Relative_Humidity >  56.46:
								if Air_Pressure <=  1010.71:
									return "UnhealthyForSensitive"
								if Air_Pressure >  1010.71:
									if Hour <=  10:
										if Air_Pressure <=  1011.86:
											return "Unhealthy"
										if Air_Pressure >  1011.86:
											return "Moderate"
									if Hour >  10:
										return "Moderate"
		if Month == "December":
			if Hour <=  9:
				if Hour <=  4:
					if Air_Pressure <=  1001.57:
						if Relative_Humidity <=  58.73:
							if Location == "Pathumthani":
								if Hour <=  0:
									if Relative_Humidity <=  56.62:
										return "Unhealthy"
									if Relative_Humidity >  56.62:
										return "Moderate"
								if Hour >  0:
									if Air_Pressure <=  999.48:
										return "Unhealthy"
									if Air_Pressure >  999.48:
										return "UnhealthyForSensitive"
							if Location == "ChiangRai":
								return "Unhealthy"
							if Location == "Tak":
								if Temperature <=  31.53:
									if Temperature <=  29.46:
										if Hour <=  2:
											return "UnhealthyForSensitive"
										if Hour >  2:
											if Relative_Humidity <=  56.34:
												return "Unhealthy"
											if Relative_Humidity >  56.34:
												if Temperature <=  29.32:
													return "UnhealthyForSensitive"
												if Temperature >  29.32:
													return "Unhealthy"
									if Temperature >  29.46:
										return "Unhealthy"
								if Temperature >  31.53:
									return "UnhealthyForSensitive"
						if Relative_Humidity >  58.73:
							if Hour <=  3:
								if Relative_Humidity <=  65.41:
									if Temperature <=  30.53:
										if Air_Pressure <=  1001.12:
											return "Moderate"
										if Air_Pressure >  1001.12:
											return "UnhealthyForSensitive"
									if Temperature >  30.53:
										if Air_Pressure <=  999.26:
											return "UnhealthyForSensitive"
										if Air_Pressure >  999.26:
											return "Moderate"
								if Relative_Humidity >  65.41:
									return "Unhealthy"
							if Hour >  3:
								if Location == "Pathumthani":
									if Relative_Humidity <=  60.47:
										if Relative_Humidity <=  59.87:
											return "UnhealthyForSensitive"
										if Relative_Humidity >  59.87:
											return "Unhealthy"
									if Relative_Humidity >  60.47:
										return "Moderate"
								if Location == "ChiangRai":
									return "UnhealthyForSensitive"
								if Location == "Tak":
									if Relative_Humidity <=  61.72:
										return "Unhealthy"
									if Relative_Humidity >  61.72:
										return "UnhealthyForSensitive"
					if Air_Pressure >  1001.57:
						if Relative_Humidity <=  53.89:
							if Air_Pressure <=  1002.66:
								return "Unhealthy"
							if Air_Pressure >  1002.66:
								return "UnhealthyForSensitive"
						if Relative_Humidity >  53.89:
							return "Moderate"
				if Hour >  4:
					if Relative_Humidity <=  53.81:
						if Location == "Pathumthani":
							return "Moderate"
						if Location == "ChiangRai":
							return "Moderate"
						if Location == "Tak":
							if Air_Pressure <=  1003.97:
								return "Moderate"
							if Air_Pressure >  1003.97:
								return "UnhealthyForSensitive"
					if Relative_Humidity >  53.81:
						if Hour <=  6:
							if Air_Pressure <=  999.87:
								if Relative_Humidity <=  63.03:
									return "Unhealthy"
								if Relative_Humidity >  63.03:
									if Relative_Humidity <=  64.97:
										return "UnhealthyForSensitive"
									if Relative_Humidity >  64.97:
										return "Unhealthy"
							if Air_Pressure >  999.87:
								if Temperature <=  28.73:
									return "Unhealthy"
								if Temperature >  28.73:
									if Hour <=  5:
										if Temperature <=  29.16:
											return "UnhealthyForSensitive"
										if Temperature >  29.16:
											return "Moderate"
									if Hour >  5:
										if Air_Pressure <=  1001.49:
											return "Unhealthy"
										if Air_Pressure >  1001.49:
											return "UnhealthyForSensitive"
						if Hour >  6:
							if Location == "Pathumthani":
								if Hour <=  8:
									return "Unhealthy"
								if Hour >  8:
									if Relative_Humidity <=  58.52:
										return "Unhealthy"
									if Relative_Humidity >  58.52:
										return "UnhealthyForSensitive"
							if Location == "ChiangRai":
								return "Unhealthy"
							if Location == "Tak":
								return "Unhealthy"
			if Hour >  9:
				if Hour <=  17:
					if Air_Pressure <=  1002.93:
						if Hour <=  11:
							if Hour <=  10:
								if Location == "Pathumthani":
									if Relative_Humidity <=  55.89:
										if Relative_Humidity <=  51.69:
											return "Unhealthy"
										if Relative_Humidity >  51.69:
											return "UnhealthyForSensitive"
									if Relative_Humidity >  55.89:
										return "Unhealthy"
								if Location == "ChiangRai":
									return "Unhealthy"
								if Location == "Tak":
									if Relative_Humidity <=  55.14:
										if Temperature <=  32.17:
											if Relative_Humidity <=  50.78:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  50.78:
												return "Unhealthy"
										if Temperature >  32.17:
											return "Moderate"
									if Relative_Humidity >  55.14:
										return "UnhealthyForSensitive"
							if Hour >  10:
								if Location == "Pathumthani":
									if Temperature <=  32.38:
										if Relative_Humidity <=  47.13:
											return "Unhealthy"
										if Relative_Humidity >  47.13:
											return "Moderate"
									if Temperature >  32.38:
										if Air_Pressure <=  999.86:
											return "UnhealthyForSensitive"
										if Air_Pressure >  999.86:
											return "Unhealthy"
								if Location == "ChiangRai":
									return "UnhealthyForSensitive"
								if Location == "Tak":
									if Air_Pressure <=  998.27:
										return "Unhealthy"
									if Air_Pressure >  998.27:
										return "UnhealthyForSensitive"
						if Hour >  11:
							if Relative_Humidity <=  50.82:
								if Air_Pressure <=  999.54:
									if Temperature <=  36.63:
										if Location == "Pathumthani":
											if Hour <=  12:
												return "UnhealthyForSensitive"
											if Hour >  12:
												if Hour <=  16:
													if Air_Pressure <=  998.07:
														return "Moderate"
													if Air_Pressure >  998.07:
														return "UnhealthyForSensitive"
												if Hour >  16:
													if Temperature <=  34.63:
														return "UnhealthyForSensitive"
													if Temperature >  34.63:
														return "Unhealthy"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											if Air_Pressure <=  997.51:
												if Hour <=  15:
													return "Unhealthy"
												if Hour >  15:
													if Relative_Humidity <=  43.38:
														if Hour <=  16:
															return "Moderate"
														if Hour >  16:
															if Relative_Humidity <=  41.08:
																return "Moderate"
															if Relative_Humidity >  41.08:
																return "Unhealthy"
													if Relative_Humidity >  43.38:
														return "UnhealthyForSensitive"
											if Air_Pressure >  997.51:
												return "Moderate"
									if Temperature >  36.63:
										return "Moderate"
								if Air_Pressure >  999.54:
									return "Moderate"
							if Relative_Humidity >  50.82:
								if Relative_Humidity <=  58.71:
									if Relative_Humidity <=  52.16:
										if Temperature <=  31.75:
											return "VeryGood"
										if Temperature >  31.75:
											return "Moderate"
									if Relative_Humidity >  52.16:
										return "Moderate"
								if Relative_Humidity >  58.71:
									if Hour <=  14:
										return "UnhealthyForSensitive"
									if Hour >  14:
										return "Unhealthy"
					if Air_Pressure >  1002.93:
						return "Moderate"
				if Hour >  17:
					if Air_Pressure <=  1001.16:
						if Temperature <=  32.42:
							if Temperature <=  28.44:
								if Hour <=  19:
									return "UnhealthyForSensitive"
								if Hour >  19:
									return "Unhealthy"
							if Temperature >  28.44:
								if Air_Pressure <=  986.17:
									if Relative_Humidity <=  55.09:
										if Temperature <=  30.59:
											if Hour <=  20:
												return "Moderate"
											if Hour >  20:
												return "Unhealthy"
										if Temperature >  30.59:
											return "Unhealthy"
									if Relative_Humidity >  55.09:
										return "UnhealthyForSensitive"
								if Air_Pressure >  986.17:
									if Relative_Humidity <=  61.84:
										if Location == "Pathumthani":
											if Air_Pressure <=  999.22:
												if Hour <=  19:
													if Hour <=  18:
														if Relative_Humidity <=  47.39:
															return "Unhealthy"
														if Relative_Humidity >  47.39:
															return "Moderate"
													if Hour >  18:
														return "Unhealthy"
												if Hour >  19:
													if Relative_Humidity <=  50.11:
														if Temperature <=  30.11:
															return "Moderate"
														if Temperature >  30.11:
															return "Unhealthy"
													if Relative_Humidity >  50.11:
														return "UnhealthyForSensitive"
											if Air_Pressure >  999.22:
												if Relative_Humidity <=  56.99:
													return "Moderate"
												if Relative_Humidity >  56.99:
													return "UnhealthyForSensitive"
										if Location == "ChiangRai":
											return "Moderate"
										if Location == "Tak":
											if Hour <=  20:
												if Hour <=  18:
													return "UnhealthyForSensitive"
												if Hour >  18:
													return "Moderate"
											if Hour >  20:
												if Air_Pressure <=  993.65:
													if Temperature <=  29.25:
														return "UnhealthyForSensitive"
													if Temperature >  29.25:
														return "Moderate"
												if Air_Pressure >  993.65:
													if Relative_Humidity <=  57.28:
														if Relative_Humidity <=  51.95:
															return "UnhealthyForSensitive"
														if Relative_Humidity >  51.95:
															if Relative_Humidity <=  55.04:
																return "Unhealthy"
															if Relative_Humidity >  55.04:
																if Temperature <=  31.22:
																	return "Unhealthy"
																if Temperature >  31.22:
																	return "UnhealthyForSensitive"
													if Relative_Humidity >  57.28:
														return "Moderate"
									if Relative_Humidity >  61.84:
										return "Unhealthy"
						if Temperature >  32.42:
							if Relative_Humidity <=  53.73:
								if Location == "Pathumthani":
									if Relative_Humidity <=  51.34:
										if Air_Pressure <=  998.1:
											return "Unhealthy"
										if Air_Pressure >  998.1:
											if Relative_Humidity <=  50.25:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  50.25:
												return "Unhealthy"
									if Relative_Humidity >  51.34:
										return "UnhealthyForSensitive"
								if Location == "ChiangRai":
									return "Unhealthy"
								if Location == "Tak":
									if Air_Pressure <=  999.31:
										if Air_Pressure <=  998.38:
											if Relative_Humidity <=  46.82:
												return "UnhealthyForSensitive"
											if Relative_Humidity >  46.82:
												if Relative_Humidity <=  48.06:
													return "Unhealthy"
												if Relative_Humidity >  48.06:
													return "UnhealthyForSensitive"
										if Air_Pressure >  998.38:
											return "Unhealthy"
									if Air_Pressure >  999.31:
										return "Moderate"
							if Relative_Humidity >  53.73:
								return "UnhealthyForSensitive"
					if Air_Pressure >  1001.16:
						if Location == "Pathumthani":
							if Hour <=  22:
								if Air_Pressure <=  1002.79:
									return "UnhealthyForSensitive"
								if Air_Pressure >  1002.79:
									if Relative_Humidity <=  51.39:
										return "Moderate"
									if Relative_Humidity >  51.39:
										return "UnhealthyForSensitive"
							if Hour >  22:
								return "Moderate"
						if Location == "ChiangRai":
							return "Moderate"
						if Location == "Tak":
							if Hour <=  21:
								if Relative_Humidity <=  51.42:
									return "UnhealthyForSensitive"
								if Relative_Humidity >  51.42:
									return "Moderate"
							if Hour >  21:
								return "UnhealthyForSensitive"
Answer = treeFunc(Air_Pressure,Hour,Location,Month,Relative_Humidity,Temperature)
print("Answer is",Answer)