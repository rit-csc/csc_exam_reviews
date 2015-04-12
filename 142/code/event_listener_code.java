// 1: anonymous class (can be done either in-line or in a method, like below)
private EventHandler<ActionEvent> getEventHandler(){
	EventHandler<ActionEvent> myEventHandler = new EventHandler<>(){
		@Override
		public void handle(ActionEvent e){
			System.out.println("#ButtonPressed2015");
		}
	}
	return myEventHandler;
}

// 2: create-your-own event handler class
class MyEventHandler implements EventHandler<ActionEvent> {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("I'm not anonymous!");
    }
}

// ...

Button myButton = new Button("Click me!");
myButton.setOnAction(getEventHandler()); // uses #1
myButton.setOnAction(new MyEventHandler()); // uses #2

