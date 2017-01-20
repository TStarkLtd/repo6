
export default class cardformDirective {
    constructor() {
        this.template = require('./cardform.html');
        this.restrict = 'EA';
        this.scope = {
			cardId: '@',
			buttonLabel: '@'
		};
        this.controller = cardformDirectiveController;
        this.controllerAs = 'ctrl';
        this.bindToController = true;
    }

    // Directive compile function
    compile() {
		
    }
    
    // Directive link function
    link() {
		
    }
}


class cardformDirectiveController {
	
	constructor(cardsData,$location) {
		'ngInject';
		console.log(cardsData);
		//console.log(this.buttonLabel);
		this.name = 'cardformDirectiveController';
		
		if (!!this.cardId) {
			this.draftCard = cardsData.getCard(this.cardId);
		} else {
			this.draftCard = {
			id: Date.now(),
			title:'',
			description:'',
			status:'todo',
			color:'#c9c9c9',
			tasks:[]
			};
		}
		
			
		this.upsertCard = () => {
			//console.log(this.draftCard);
			let cards = cardsData.upsertCards(this.draftCard);
			//console.log(cards);
			$location.path("/");
		};
		
		this.cancel = () => {
			$location.path("/");
		};

	}
	
}
