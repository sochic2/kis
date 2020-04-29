library(shiny)
library(leaflet)

r_colors <- rgb(t(col2rgb(colors()) / 255))
names(r_colors) <- colors()

ui <- fluidPage(
    leafletOutput("mymap"),
    p(),
    actionButton("recalc", "New points"),
    p(),
    hr(),
    
    column(1,
           dataTableOutput('mytable')
    )    
    

)



server <- function(input, output, session) {
    
    points <- eventReactive(input$recalc, {
        cbind(rnorm(40) * 2 + 13, rnorm(40) + 48)
    }, ignoreNULL = FALSE)
    
    output$mymap <- renderLeaflet({
        leaflet() %>%
            setView(lng=127.3598557, lat=36.3655591, zoom=16) %>%
            addProviderTiles('OpenStreetMap.HOT')
    })
    
    
    rock = data.frame()
    output$mytable = renderDataTable(read.csv('data.csv'))
    
    
}



shinyApp(ui,  server)