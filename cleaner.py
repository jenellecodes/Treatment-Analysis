def clean_data(data):
  cleaned_data = []
  for x in data[1:]:
      x = x.replace("\n","")
      cleaned_data.append(float(x))
   
  return cleaned_data