from langgraph.graph import START,END,StateGraph
import nodes

workflow=StateGraph(nodes.State)

workflow.add_node('transcript',nodes.FetchTranscript)
workflow.add_node('blog',nodes.BlogGenerate)
workflow.add_node('summary',nodes.SummaryGenerate)

workflow.add_edge(START,'transcript')
workflow.add_edge('transcript','summary')
workflow.add_edge('summary','blog')
workflow.add_edge('blog',END)

graph=workflow.compile()

# video_id='https://www.youtube.com/watch?v=iWS9ogMPOI0'
# print(graph.invoke({'video_id':video_id})['blog'])