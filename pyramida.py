def on_on_chat():
    for index in range(3):
        for index2 in range(10):
            agent.destroy(FORWARD)
            agent.destroy(UP)
            agent.place(BACK)
            agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
    for index6 in range(4):
        for index3 in range(9):
            agent.destroy(FORWARD)
            agent.destroy(UP)
            agent.place(BACK)
            agent.move(FORWARD, 1)
            agent.turn(LEFT_TURN)
    for index4 in range(3):
        for index5 in range(9):
            agent.destroy(FORWARD)
            agent.destroy(UP)
            agent.place(BACK)
            agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
player.on_chat("run", on_on_chat)

