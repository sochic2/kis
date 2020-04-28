#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("K-Means"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("points",
                        "Number of points:",
                        min = 100,
                        max = 30000,
                        value = 150),
            
            sliderInput("cluster",
                        "Number of clusters:",
                        min = 3,
                        max = 10,
                        value = 5)
        ),
        

        mainPanel(
           plotOutput("distPlot")
           
         
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

    output$distPlot <- renderPlot({

        x = rnorm(input$points)
        y = rnorm(input$points)
        
        t_data = data.frame(x=x, y=y)
        
        plot(x, y, cex=0.1)
        
        num_of_clusters = input$cluster
        
        res = kmeans(t_data, num_of_clusters)
        
        for(i in 1:num_of_clusters) {
            
            for(j in which(res$cluster==i)){
                lines(c(res$centers[i,1], t_data[j,1]),
                      c(res$centers[i,2], t_data[j,2]),
                      col=i+3)
            }
            
            points(res$centers[i,1], res$centers[i, 2],
                   col='red', cex=2)
            
            text(res$centers[i,1],res$centers[i,2],
                 labels=paste('center-',i), pos=3,
                 cex=0.7)
        }

    })
}

# Run the application 
shinyApp(ui = ui, server = server)
