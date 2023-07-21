import csv
with open('C:/Users/pouria zarrin/Desktop/medical-insurance/insurance.csv' , newline='') as insurance_data:
    data = list(csv.DictReader(insurance_data))


#average cost of all the individuals in the database
def cost_average():
    all_cost = 0
    counter = 0
    for individual in data :
        cost = float(individual['charges'])
        all_cost += cost
        counter += 1
    return (all_cost/counter)


#average cost of female and male
def gender_analysis():
    men_counter = 0
    men_cost = 0
    women_counter = 0
    women_cost = 0
    for individual in data:
        if individual['sex'] == 'male':
            men_counter += 1
            cost = float(individual['charges'])
            cost = round(cost)
            men_cost += cost
        else:
            women_counter += 1
            cost = float(individual['charges'])
            cost = round(cost)
            women_cost += cost
    print ('there is' , men_counter , 'men in the database with average cost of' , round(men_cost/men_counter) , 'and there is' , women_counter , 'female with average cost of' , round(women_cost/women_counter))

#average cost of smokers and non smokers
def smoker_analysis():
    smoker_cost = 0
    smoker_counter = 0
    non_smoker_cost = 0
    non_smoker_counter = 0
    for individual in data:
        if individual['smoker'] == 'yes' :
            smoker_cost += float(individual['charges'])
            smoker_counter += 1
        else :
            non_smoker_cost += float(individual['charges'])
            non_smoker_counter += 1
    print ('there are',smoker_counter,'smoker individuals in the database with average insurance cost of',round(smoker_cost/smoker_counter),'and there are',non_smoker_counter,'non smokers with average insurance cost of',round(non_smoker_cost/non_smoker_counter))


#counter of individuals in each region
def region_analysis():
    north_east = 0
    north_west = 0
    south_east = 0
    south_west = 0
    for individual in data:
        if individual['region'] == 'northeast' :
            north_east += 1
        if individual['region'] == 'northwest' :
            north_west += 1
        if individual['region'] == 'southeast' :
            south_east += 1
        if individual['region'] == 'southwest' :
            south_west += 1
    print ('individual counts in each region')
    print (north_east,'individuals in norht east')
    print (north_west,'individuals in north_west')
    print (south_east,'individuals in south_east')
    print (south_west,'individuals in south_west')

#average insurance costs of individuals with different number of children
def child_analysis():
    children_count = {}
    children_cost = {}
    children_cost_average = {}
    for individual in data:
        x = individual['children']
        if x in children_count :
            children_count[x] += 1
        else :
            children_count[x] = 1
        if x in children_cost :
            children_cost[x] += round(float(individual['charges']))
        else :
            children_cost[x] = round(float(individual['charges']))
    child_index_cost_value = list(children_cost.values())
    child_index_cost_keys = list(children_cost.keys())
    child_index_count = list(children_count.values())
    count = 0
    for individual in child_index_cost_keys:
        children_cost[individual] = round(float(child_index_cost_value[count] / child_index_count[count]))
        count += 1


    child_index_cost_value = list(children_cost.values())
    child_data = []
    for i in range(len(child_index_cost_keys)):
        print ('there are' , child_index_count[i] , 'people with' , child_index_cost_keys[i] , 'number of children that have' , child_index_cost_value[i] , 'average of insurance expenses')
        child_data.append({'children':int(child_index_cost_keys[i]) , 'individuals':child_index_count[i] , 'average cost':child_index_cost_value[i]})
child_analysis()
