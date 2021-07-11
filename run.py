from log import Log

def init_t(l, start, end, init_temp=0):
  def inner():
    t = [init_temp] * l
    t[0] = start
    t[l - 1] = end
    return t
  return inner

def run(lnt, t_count, t_start, t_end, log, insulated=False, init_temp=0, del_t=0, _lambda=0):
  init = init_t(lnt, t_start, t_end, init_temp)
  t = init()

  results = [t]

  for l in range(int(t_count / del_t)):
    new_t = init()
    t = results[l]
    if not insulated:
      new_t[0] = round(t[0] - _lambda * (2 * t[1] - 2 * t[0] + 4), 4)
    for i in range(1, lnt - 1):
      new_t[i] = round(t[i] + _lambda * (t[i + 1] - 2 * t[i] + t[i - 1]), 4)
    if not insulated:
      new_t[lnt - 1] = round(t[lnt - 1] - _lambda * (2 * t[lnt - 2] - 2 * t[lnt - 1] + 4), 4)
    results.append(new_t)

  l = Log(log[0])
  l.prwrite(results, title=log[1])

if __name__ == '__main__':
  run(
    lnt=6,
    t_count=12,
    t_start=100,
    t_end=50,
    log=['insulated', 'Insulated'],
    insulated=True,
    del_t=0.1,
    _lambda=0.020875
  )

  run(
    lnt=6,
    t_count=0.5,
    t_start=50,
    t_end=50,
    log=['open', 'Open'],
    init_temp=50,
    del_t=0.1,
    _lambda=0.020875,
  )
