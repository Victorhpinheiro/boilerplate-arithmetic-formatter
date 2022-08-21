def arithmetic_arranger(problems,answer = False):

    #Error Handling
    if len(problems) > 5:
        return "Error: Too many problems."
    top = []
    bot = []
    ans = []
    sig = []
    mid = []

    for item in problems:
        tmp = item.split()

        if tmp[1] != "+" and tmp[1] != "-":
            return "Error: Operator must be '+' or '-'."

        elif len(tmp[0]) > 4 or len(tmp[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if tmp[1] == "+":
          try:
              ans.append(str(int(tmp[0]) + int(tmp[2])))
          except:
              return "Error: Numbers must only contain digits."
        if tmp[1] == "-":
          try:
              ans.append(str(int(tmp[0]) - int(tmp[2])))
          except:
              return "Error: Numbers must only contain digits."

        top.append(tmp[0])
        bot.append(tmp[2])
        sig.append(tmp[1])

    #prepare rows
    for i in range(0, len(top)):
        st = len(top[i])
        sb = len(bot[i])
        mx = max(st, sb)

        while len(top[i]) < mx + 2:
            top[i] = " " + top[i]

        repeat = mx + 2
        mid.append("-" * repeat)

        while len(bot[i]) < mx:
            bot[i] = " " + bot[i]
        bot[i] = sig[i] + " " + bot[i]

        while len(ans[i]) < mx + 2:
            ans[i] = " " + ans[i]

        form = []
        form.append("    ".join(top))
        form.append("    ".join(bot))
        form.append("    ".join(mid))
        if not answer:
            arranged_problems = "\n".join(form)
        else:
            form.append("    ".join(ans))
            arranged_problems = "\n".join(form)

    

    return arranged_problems




# arithmetic_arranger(test)

