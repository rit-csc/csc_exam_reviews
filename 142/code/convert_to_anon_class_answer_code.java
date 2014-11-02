JButton okButton = new JButton("ok");
okButton.addActionListener(new ActionListener() {
	public void actionPerformed(ActionEvent e) {
		System.exit(0);
	}
});

JButton cancelButton = new JButton("cancel");
cancelButton.addActionListener(new ActionListener() {
	public void actionPerformed(ActionEvent e) {
		log.debug("User pressed cancel.");
	}
});