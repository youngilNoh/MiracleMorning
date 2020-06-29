days = {"Mon", "Tue", "Wed", "Thu", "Fri"}

for day in days:
  # 강의에선 day is "Wed"로 나오는데, 오류가 생겼다.
  if day == "Wed":
    break
  else:
    print(day)