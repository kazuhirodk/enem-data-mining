import pandas as pd

def extractor(rules_table):
  organized_rules = []

  for count in range(rules_table.shape[0]):
    for rule in rules_table.iloc[count, 2]:
      organized_rule = {
        'items_base': list(rule.items_base),
        'items_add': list(rule.items_add),
        'support': rules_table.iloc[count, 1],
        'confidence': rule.confidence,
        'lift': rule.lift
      }
      organized_rules.append(organized_rule)

  return pd.DataFrame(organized_rules, columns=['items_base', 'items_add', 'support', 'confidence', 'lift'])
