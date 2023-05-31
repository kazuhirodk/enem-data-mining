def extractor(rules_table):
  organized_rules = pd.DataFrame(columns = ('items_base', 'items_add', 'support', 'confidence', 'lift'))
  count = 0
  index = 0

  while count < rules_table.shape[0]:
    for rule in rules_table.iloc[count, 2]:
      organized_rules.loc[index, 'items_base'] = list(rule.items_base)
      organized_rules.loc[index, 'items_add'] = list(rule.items_add)
      organized_rules.loc[index, 'support'] = rules_table.iloc[count, 1]
      organized_rules.loc[index, 'confidence'] = rule.confidence
      organized_rules.loc[index, 'lift'] = rule.lift
      index += 1
    count += 1
  
  return organized_rules
