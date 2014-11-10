class ControlListener implements ActionListener{
	public void actionPerformed(ActionEvent e) {
		if((JButton)e.getSource()).getText().equals("ok")) {
			System.exit(0);
		} else {
			log.debug("User pressed cancel.");
		}
	}
}

ControlListener cListener = new ControlListener();
JButton okButton = new JButton("ok");
JButton cancelButton = new JButton("cancel");
okButton.addActionListener(cListener);
cancelButton.addActionListener(cListener);
