﻿James=list()
James=['unwilling to depart from examples of the most revered authority', 'I avail myself of the occasion now presented to express the profound impression made on me by the call of my country to the station to the duties of which I am about to pledge myself by the most solemn of sanctions', 'So distinguished a mark of confidence', 'proceeding from the deliberate and tranquil suffrage of a free and virtuous nation', 'would under any circumstances have commanded my gratitude and devotion', 'as well as filled me with an awful sense of the trust to be assumed', 'Under the various circumstances which give peculiar solemnity to the existing period', 'I feel that both the honor and the responsibility allotted to me are inexpressibly enhanced', 'The present situation of the world is indeed without a parallel', 'and that of our own country full of difficulties', 'The pressure of these, too, is the more severely felt because they have fallen upon us at a moment when the national prosperity being at a height not before attained', 'the contrast resulting from the change has been rendered the more striking', 'Under the benign influence of our republican institutions, and the maintenance of peace with all nations whilst so many of them were engaged in bloody and wasteful wars, the fruits of a just policy were enjoyed in an unrivaled growth of our faculties and resources', 'Proofs of this were seen in the improvements of agriculture, in the successful enterprises of commerce, in the progress of manufacturers and useful arts, in the increase of the public revenue and the use made of it in reducing the public debt, and in the valuable works and establishments everywhere multiplying over the face of our land', 'It is a precious reflection that the transition from this prosperous condition of our country to the scene which has for some time been distressing us is not chargeable on any unwarrantable views, nor, as I trust, on any involuntary errors in the public councils', 'Indulging no passions which trespass on the rights or the repose of other nations', 'it has been the true glory of the United States to cultivate peace by observing justice, and to entitle themselves to the respect of the nations at war by fulfilling their neutral obligations with the most scrupulous impartiality', 'If there be candor in the world, the truth of these assertions will not be questioned', 'posterity at least will do justice to them', 'This unexceptionable course could not avail against the injustice and violence of the belligerent powers', 'In their rage against each other, or impelled by more direct motives, principles of retaliation have been introduced equally contrary to universal reason and acknowledged law', 'How long their arbitrary edicts will be continued in spite of the demonstrations that not even a pretext for them has been given by the United States', 'and of the fair and liberal attempt to induce a revocation of them', 'can not be anticipated', 'Assuring myself that under every vicissitude the determined spirit and united councils of the nation will be safeguards to its honor and its essential interests', 'I repair to the post assigned me with no other discouragement than what springs from my own inadequacy to its high duties', 'If I do not sink under the weight of this deep conviction it is because I find some support in a consciousness of the purposes and a confidence in the principles which I bring with me into this arduous service', 'To cherish peace and friendly intercourse with all nations having correspondent dispositions', 'to maintain sincere neutrality toward belligerent nations', 'to prefer in all cases amicable discussion and reasonable accommodation of differences to a decision of them by an appeal to arms', 'to exclude foreign intrigues and foreign partialities', 'so degrading to all countries and so baneful to free ones', 'to foster a spirit of independence too just to invade the rights of others', 'too proud to surrender our own', 'too liberal to indulge unworthy prejudices ourselves and too elevated not to look down upon them in others', 'to hold the union of the States as the basis of their peace and happiness', 'to support the Constitution', 'which is the cement of the Union', 'as well in its limitations as in its authorities', 'to respect the rights and authorities reserved to the States and to the people as equally incorporated with and essential to the success of the general system', 'to avoid the slightest interference with the right of conscience or the functions of religion', 'so wisely exempted from civil jurisdiction', 'to preserve in their full energy the other salutary provisions in behalf of private and personal rights', 'and of the freedom of the press', 'to observe economy in public expenditures', 'to liberate the public resources by an honorable discharge of the public debts', 'to keep within the requisite limits a standing military force', 'always remembering that an armed and trained militia is the firmest bulwark of republics - that without standing armies their liberty can never be in danger', 'nor with large ones safe', 'to promote by authorized means improvements friendly to agriculture, to manufactures, and to external as well as internal commerce', 'to favor in like manner the advancement of science and the diffusion of information as the best aliment to true liberty', 'to carry on the benevolent plans which have been so meritoriously applied to the conversion of our aboriginal neighbors from the degradation and wretchedness of savage life to a participation of the improvements of which the human mind and manners are susceptible in a civilized state', 'as far as sentiments and intentions such as these can aid the fulfillment of my duty', 'they will be a resource which can not fail me', 'It is my good fortune, moreover', 'to have the path in which I am to tread lighted by examples of illustrious services successfully rendered in the most trying difficulties by those who have marched before me', 'Of those of my immediate predecessor it might least become me here to speak', 'I may, however, be pardoned for not suppressing the sympathy with which my heart is full in the rich reward he enjoys in the benedictions of a beloved country', 'gratefully bestowed or exalted talents zealously devoted through a long career to the advancement of its highest interest and happiness', 'But the source to which I look or the aids which alone can supply my deficiencies is in the well-tried intelligence and virtue of my fellow-citizens', 'and in the counsels of those representing them in the other departments associated in the care of the national interests', 'In these my confidence will under every difficulty be best placed', 'next to that which we have all been encouraged to feel in the guardianship and guidance of that Almighty Being whose power regulates the destiny of nations', 'whose blessings have been so conspicuously dispensed to this rising Republic', 'and to whom we are bound to address our devout gratitude for the past', 'as well as our fervent supplications and best hopes for the future']
def Jamesmuch():
 d=dict()
 for line in James:
  words=line.split()
  for c in words:
   if c not in d:
    d[c]=1
   else:
    d[c]=d[c]+1
 for w in range(0,len(d)):
  if d.values()[w]>=10:
   print 'James used: ', d.keys()[w], d.values()[w]

Jimmy=list()
Jimmy=['for myself and for our Nation', 'I want to thank my predecessor for all he has done to heal our land', 'In this outward and physical ceremony we attest once again to the inner and spiritual strength of our Nation', 'As my high school teacher, Miss Julia Coleman, used to say', "We must adjust to changing times and still hold to unchanging principles", 'Here before me is the Bible used in the inauguration of our first President, in 1789', 'and I have just taken the oath of office on the Bible my mother gave me a few years ago', 'opened to a timeless admonition from the ancient prophet Micah', 'He hath showed thee, O man', 'what is good', 'and what doth the Lord require of thee', 'but to do justly, and to love mercy, and to walk humbly with thy God', 'This inauguration ceremony marks a new beginning', 'a new dedication within our Government', 'and a new spirit among us all', 'A President may sense and proclaim that new spirit', 'but only a people can provide it', 'Two centuries ago our Nation's birth was a milestone in the long quest for freedom', 'but the bold and brilliant dream which excited the founders of this Nation still awaits its consummation', 'I have no new dream to set forth today, but rather urge a fresh faith in the old dream', 'Ours was the first society openly to define itself in terms of both spirituality and of human liberty', 'It is that unique self-definition which has given us an exceptional appeal', 'but it also imposes on us a special obligation', 'to take on those moral duties which', 'when assumed', 'seem invariably to be in our own best interests', 'You have given me a great responsibility-to stay close to you, to be worthy of you, and to exemplify what you are', 'Let us create together a new national spirit of unity and trust. Your strength can compensate for my weakness', 'and your wisdom can help to minimize my mistakes', 'Let us learn together and laugh together and work together and pray together', 'confident that in the end we will triumph together in the right', 'The American dream endures', 'We must once again have full faith in our country-and in one another', 'I believe America can be better', 'We can be even stronger than before', 'Let our recent mistakes bring a resurgent commitment to the basic principles of our Nation', 'for we know that if we despise our own government we have no future', 'We recall in special times when we have stood briefly, but magnificently, united', 'In those times no prize was beyond our grasp', 'But we cannot dwell upon remembered glory', 'We cannot afford to drift', 'We reject the prospect of failure or mediocrity or an inferior quality of life for any person', 'Our Government must at the same time be both competent and compassionate', 'We have already found a high degree of personal liberty', 'and we are now struggling to enhance equality of opportunity', 'Our commitment to human rights must be absolute, our laws fair, our natural beauty preserved', 'the powerful must not persecute the weak', 'and human dignity must be enhanced', 'We have learned that more is not necessarily better', 'that even our great Nation has its recognized limits', 'and that we can neither answer all questions nor solve all problems', 'We cannot afford to do everything, nor can we afford to lack boldness as we meet the future', 'So, together, in a spirit of individual sacrifice for the common good, we must simply do our best', 'Our Nation can be strong abroad only if it is strong at home', 'And we know that the best way to enhance freedom in other lands is to demonstrate here that our democratic system is worthy of emulation', 'To be true to ourselves, we must be true to others', 'We will not behave in foreign places so as to violate our rules and standards here at home', 'for we know that the trust which our Nation earns is essential to our strength', 'The world itself is now dominated by a new spirit', 'Peoples more numerous and more politically aware are craving and now demanding their place in the sun', 'not just for the benefit of their own physical condition', 'but for basic human rights', 'The passion for freedom is on the rise', 'Tapping this new spirit, there can be no nobler nor more ambitious task for America to undertake on this day of a new beginning than to help shape a just and peaceful world that is truly humane', 'We are a strong nation, and we will maintain strength so sufficient that it need not be proven in combat', 'a quiet strength based not merely on the size of an arsenal, but on the nobility of ideas', 'We will be ever vigilant and never vulnerable, and we will fight our wars against poverty, ignorance, and injustice for those are the enemies against which our forces can be honorably marshaled', 'We are a purely idealistic Nation, but let no one confuse our idealism with weakness', 'Because we are free we can never be indifferent to the fate of freedom elsewhere', 'Our moral sense dictates a clearcut preference for these societies which share with us an abiding respect for individual human rights', 'We do not seek to intimidate, but it is clear that a world which others can dominate with impunity would be inhospitable to decency and a threat to the well-being of all people', 'The world is still engaged in a massive armaments race designed to ensure continuing equivalent strength among potential adversaries', 'We pledge perseverance and wisdom in our efforts to limit the world's armaments to those necessary for each nation's own domestic safety', 'And we will move this year a step toward ultimate goal the elimination of all nuclear weapons from this Earth', 'We urge all other people to join us', 'for success can mean life instead of death', 'ithin us, the people of the United States, there is evident a serious and purposeful rekindling of confidence', 'And I join in the hope that when my time as your President has ended, people might say this about our Nation', 'that we had remembered the words of Micah and renewed our search for humility, mercy, and justice', 'that we had torn down the barriers that separated those of different race and region and religion, and where there had been mistrust, built unity, with a respect for diversity', ' that we had found productive work for those able to perform it', 'that we had strengthened the American family, which is the basis of our society', 'that we had ensured respect for the law, and equal treatment under the law, for the weak and the powerful, for the rich and the poor', 'and that we had enabled our people to be proud of their own Government once again', 'I would hope that the nations of the world might say that we had built a lasting peace', 'built not on weapons of war but on international policies which reflect our own most precious values', 'These are not just my goals, and they will not be my accomplishments, but the affirmation of our Nation's continuing moral strength and our belief in an undiminished, ever-expanding American dream']
def Jimmymuch():
 d=dict()
 for line in Jimmy:
  words=line.split()
  for c in words:
   if c not in d:
    d[c]=1
   else:
    d[c]=d[c]+1
 for w in range(0,len(d)):
  if d.values()[w]>=10:
   print 'Jimmy used: ', d.keys()[w], d.values()[w]

def lab10():
 Jamesmuch()
 Jimmymuch()

def main():
 lab10()

main()
raw_input('201611069_w10_hw_second')