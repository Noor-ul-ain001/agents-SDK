📝 to_input_list() Method

The to_input_list() method is used to convert any input into a proper list format. If you give it a single string, it wraps it inside a list. If you already provide a list, it keeps it the same. And if you pass an agent’s output, it converts that into an AgentInput list that the next agent can easily understand. In short, this method makes sure that the input is always in a list form so it can be safely passed between agents.
